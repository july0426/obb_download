#coding:utf8
import requests,time,MySQLdb,re
'''从数据库提取代理'''
def get_proxy():
    db = MySQLdb.connect('localhost', 'root', '123456', 'test')
    cursor = db.cursor()
    sql = "select * from pngtree_proxy order by status asc limit 1"
    try:
        cursor.execute(sql)
        proxies = cursor.fetchone()
        # 更新代理时间戳
        sql = "update pngtree_proxy set status=%d where id=%d" % (int(time.time()), proxies[0])
        cursor.execute(sql)
        proxy = {
            'http': 'http://%s' % proxie,
            'https': 'https://%s' % proxie,
        }
        db.commit()
        return proxy
    except Exception, e:
        print sql
        print str(e)
        db.rollback()
        proxy = 0
        return proxy
'''根据传入的URL,下载文件,并将文件路径保存到数据库'''
def download(url,file_name,id):
    db = MySQLdb.connect('localhost', 'root', '123456', 'test')
    cursor = db.cursor()
    start = time.time()
    # proxy = get_proxy()
    proxy = 0
    if proxy:
        r = requests.get(url, stream=True,proxies=proxy)
    # 采用流式请求,对内容进行迭代
    else:
        r = requests.get(url, stream=True)
    # 分块写入文件
    with open(file_name, "wb") as code:
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                code.write(chunk)
    end = time.time()
    used_time = end - start
    print '文件下载完成,用时%s秒' % used_time
    sql = 'update download set status=2,path="%s" where id=%s' % (file_name,id)
    try:
        cursor.execute(sql)
        db.commit()
        print '本地存储路径更新完成'
    except Exception, e:
        db.rollback()
        print str(e)
def apkhouse(data):
    url = data[1]
    print url
    s = requests.session()
    proxy = get_proxy()
    if proxy:
        s.proxies = proxy
    ress = s.get(url)
    re_com = re.compile(r'class="goog-inline-block jfk-button jfk-button-action" href="(.*?)">')
    url_down = re.search(re_com, ress.text).group(1).replace('amp;', '')
    urls = 'https://docs.google.com' + url_down
    print urls
    a = ress.text
    re_type = re.compile(r'<span class="uc-name-size"><a href="https://docs.google.com.*?">(.*?)</a>')
    file_type = re.search(re_type, a).group(1)[-4:]
    id = data[0]
    file_name = '/users/qiyue/myxuni/pngtree/obb_download/' + data[2] + file_type
    print file_name
    start = time.time()
    r = s.get(urls, stream=True)
    with open(file_name, "wb") as code:
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                code.write(chunk)
    end = time.time()
    used_time = end - start
    print '文件下载完成,用时%s秒' % used_time
    db = MySQLdb.connect('localhost', 'root', '123456', 'test')
    cursor = db.cursor()
    sql = 'update download set status=2,path="%s" where id=%s' % (file_name, id)
    try:
        cursor.execute(sql)
        db.commit()
        print '本地存储路径更新完成'
    except Exception, e:
        db.rollback()
        print str(e)
def zippyshare(data):
    url = data[1]
    print url
    proxy = get_proxy()
    if proxy:
        res = requests.get(url,proxies=proxy)
    else:
        res = requests.get(url)
    text = res.text
    re_url = re.compile(r'document\.getElementById\(\'dlbutton\'\)\.href = (.*?);')
    url_data = re.search(re_url,text)
    if url_data:
        url_data = url_data.group(1)
        print url_data
        re_num = re.compile(r'\((.*?)\)')
        num = re.search(re_num, url_data)
        num = num.group(1)
        print num
        nu = eval(num)
        print nu
        url_data = url_data.split('"')
        print url_data
        url = 'http://www101.zippyshare.com' + url_data[1] + str(nu) + url_data[-2]
        print url
        file_type = url[-4:]
        id = data[0]
        file_name = '/users/qiyue/myxuni/pngtree/obb_download/' + data[2] + file_type
        print file_name
        download(url,file_name,id)
def android(data):
    url = data[1]
    print url
    proxy = get_proxy()
    if proxy:
        text = requests.get(url,proxies=proxy).text
    else:
        text = requests.get(url).text
    re_url = re.compile(r'<div id=download></div><a href=(.*?)><input')
    url = re.search(re_url,text)
    re_type = re.compile(r'<div class="title">(.*?)</div>')
    file_type = re.search(re_type,text)
    if url:
        if file_type:
            url = url.group(1)
            file_type = file_type.group(1).strip()[-4:]
            id = data[0]
            file_name = '/users/qiyue/myxuni/pngtree/obb_download/' + data[2] + file_type
            print file_name
            download(url,file_name,id)
    else:
        print 'android网站,未匹配到下载的URL'
def dropapk(data):
    url = data[1]
    print url
    datas = {
        'op': 'download2',
        'id': url.split('/')[-1],
        'rand': '',
        'referer': url,
        'method_free': 'Free Download',
        'method_premium': '',
        'adblock_detected': '0',
    }
    proxy = get_proxy()
    if proxy:
        text = requests.post(url,data = datas,proxies=proxy).text
    else:
        text = requests.post(url,data = datas).text
    re_url = re.compile(r'<a href="(.*?)"><img src="https://dropapk.com/images_mega/down_final.png"')
    url = re.search(re_url,text)
    if url:
        url = url.group(1)
        file_type = url[-4:]
        id = data[0]
        file_name = '/users/qiyue/myxuni/pngtree/obb_download/' + data[2] + file_type
        print file_name
        download(url,file_name,id)
    else:
        print 'dropapk.com网站的下载链接没有匹配到'
def farsroid(data):
    url = data[1]
    print url
    file_type = url[-4:]
    id = data[0]
    file_name = '/users/qiyue/myxuni/pngtree/obb_download/' + data[2] +file_type
    print file_name
    download(url,file_name,id)
'''链接数据库,取出URL及文件名称'''
def get_data():
    db = MySQLdb.connect('localhost', 'root', '123456', 'test')
    cursor = db.cursor()
    sql = 'select id,url,name from download where status=0 limit 1'
    try:
        cursor.execute(sql)
        record = cursor.fetchone()
        db.commit()
        if record:
            sql = 'update download set status=1 where id=%s' % record[0]
            try:
                cursor.execute(sql)
                db.commit()
            except Exception, e:
                db.rollback()
                print str(e)
            print record
            return record
        else:
            return 0
    except Exception, e:
        db.rollback()
        print str(e)
if __name__ == '__main__':
    # 获取要下载的链接,从数据库中
    data = get_data()
    # 根据取出的URL,获取到网站名称,根据网站名称,调用相应的函数进行处理,下载文件
    if data:
        def_name = data[1].split('/')[2]
        if def_name == 'apkhouse.com':
            apkhouse(data)
        elif def_name == 'www101.zippyshare.com':
            zippyshare(data)
        elif def_name == 'android-1.com':
            android(data)
        elif def_name == 'dropapk.com':
            dropapk(data)
        elif def_name == 'www.dl.farsroid.com':
            farsroid(data)
        else:
            print 'url不在该脚本处理范围内'
    else:
        print '没取到数据'


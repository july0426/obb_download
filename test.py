#coding:utf8
import re
a = 'http://apkhouse.com/?dl_id=645'
b = a.split('/')
print b[2]
text = '''document.getElementById('dlbutton').href = "/d/Iuu4n96Q/" + (741327 % 51245 + 741327 % 913) + "/com.gamedevltd.modernstrike.zip";拼好后的地址http://www101.zippyshare.com/d/Iuu4n96Q/24781/com.gamedevltd.modernstrike.zip'''
re_url = re.compile(r'document\.getElementById\(\'dlbutton\'\)\.href = (.*?);')
url_data = re.search(re_url,text)
if url_data:
    url_data = url_data.group(1)
    print url_data
    re_num = re.compile(r'\((.*?)\)')
    num = re.search(re_num,url_data)
    num =  num.group(1)
    print num
    nu = eval(num)
    print nu
    url_data = url_data.split('"')
    print url_data
    url = 'http://www101.zippyshare.com' + url_data[1] + str(nu) + url_data[-2]
    print url
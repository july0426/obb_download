#coding:utf8
from gevent import monkey; monkey.patch_socket()
import urllib2,time,gevent
def get_file(urls):
    url = urls.keys()[0]
    f = urllib2.urlopen(url)
    start = time.time()
    filename = '/users/qiyue/myxuni/pngtree/obb_download/' + str(int(time.time())) +'.' + urls.values()[0]
    print filename
    with open(filename, "wb") as code:
        code.write(f.read())
    end = time.time()
    print (end - start)

if __name__ == '__main__':
    start = time.time()
    urls = [
        {'http://server01.dropapk.com:182/d/apc7next4tcdvbi4rgyzhxac2ouhz2v4qpplxuqh3vaehjiqexlsfstslc3tt4g7u2lditw2/com.blayzegames.iosfps.zip': 'zip'},
        {'https://www.4sync.com/web/directDownload/U13cYaUq/37mzmToo.4331175374f1da932dea415de6b08e15': 'apk'},
        {'http://www.dl.farsroid.com/game/Lost-Lands-5-Full-1.0.1(www.Farsroid.com).zip': 'zip'},
        {'http://www101.zippyshare.com/d/Iuu4n96Q/50470/com.gamedevltd.modernstrike.zip': 'zip'},
        {'https://docs.google.com/uc?export=download&confirm=dU2B&id=1JQySKZYR8KLRKtcIz7WnzuqezjowQT6k': 'zip'},
    ]
    lists = []
    for url in urls:
        lists.append(gevent.spawn(get_file,url))
    gevent.joinall(lists)
    end = time.time()
    print '最终的时间',(end - start)

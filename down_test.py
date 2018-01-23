# coding:utf8
from gevent import monkey; monkey.patch_socket()
import urllib2,time,gevent,requests,re,random
s = requests.session()
user_agentss = [
    'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
    'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
    'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56S',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)'
]
data = {
    'login':'july0426',
    'pass':'200702025qiyue'
}
# headers = {
#     'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'accept-encoding':'gzip, deflate, br',
#     'accept-language':'zh-CN,zh;q=0.9',
#     'cache-control':'max-age=0',
#     'cookie':'download_warning_03457638012327761959_1JQySKZYR8KLRKtcIz7WnzuqezjowQT6k=s7ON; CONSENT=YES+FR.zh-CN+V13; S=explorer=Uh45Z-HK_-a5YHH2OZBen2PdwmgRug3d; 1P_JAR=2018-1-22-6; SID=rQWi5svOTW4jYZ9R-twnnXI_kBC9ocXzx_GMzhO2T9vFUnhKO8bC8_EfY43FhR8nfYQD6Q.; HSID=AOWAq-IMibWBrNsTl; SSID=AhT-RPvGWUymPsV8n; APISID=sAPvrCH3cRipNoop/AV_kXaRsNaObAE_E-; SAPISID=e1uUIIxuGBZZDQKH/A5u1iJHiFRACPVIPk; NID=122=gU624TPmUkUHUN6SuyP3siU2oXs7ZELuG9hdP4ZhcPkb-anFfLHlSuJJJK1K7g7ktpecEMKT8w2ko7Qf6cY6Ykt7SL2UGSO-4p05vsGS3t484H45A0TEMb43DwhIbGn3_E5fv_iNxfvombSeyzFjIrkFRGfmoqvBUCTYEsxJDpIYBEyjKQBZUfbqxnQEHOmLNV8jPvAllypPKCo1i58aFk2lSYufFTc1MWDlIrR5nCOHV2m1iaB2y6B6y2V4F18-tN5lWl7ed5BXIwKLctF93pI; SIDCC=AAiTGe8haYqSo8uW8e5XaSg0QWidkxlB5uZyo34jSmRzRtENIE5xjB9zVB67mWPqHu_uLTdthRA',
#     'upgrade-insecure-requests':'1',
#     'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
#     'x-chrome-connected':'id=113418274569883164278,mode=0,enable_account_consistency=false',
#     'x-chrome-uma-enabled':'1',
#     'x-client-data':'CJK2yQEIo7bJAQjEtskBCKuYygEI+pzKAQipncoBCKijygE='
# }
headers = {
    'user-agent': random.choice(user_agentss),
}
print headers
s.headers = headers

urls = [
{'http://server01.dropapk.com:182/d/apc7next4tcdvbi4rgyzhxac2ouhz2v4qpplxuqh3vaehjiqexlsfstslc3tt4g7u2lditw2/com.blayzegames.iosfps.zip':'zip'},
{'https://www.4sync.com/web/directDownload/U13cYaUq/37mzmToo.4331175374f1da932dea415de6b08e15':'apk'},
{'http://www.dl.farsroid.com/game/Lost-Lands-5-Full-1.0.1(www.Farsroid.com).zip':'zip'},
{'http://www101.zippyshare.com/d/Iuu4n96Q/50470/com.gamedevltd.modernstrike.zip':'zip'},
{'https://docs.google.com/uc?export=download&confirm=MCse&id=1JQySKZYR8KLRKtcIz7WnzuqezjowQT6k':'zip'},
    ]
# url_dict = urls[1]
# url = url_dict.keys()[0]
url = 'https://docs.google.com/uc?export=download&confirm=MCse&id=1JQySKZYR8KLRKtcIz7WnzuqezjowQT6k'
print url

ress = s.get(url,headers=headers)
print ress.text
re_com = re.compile(r'class="goog-inline-block jfk-button jfk-button-action" href="(.*?)">')
url_down = re.search(re_com,ress.text).group(1).replace('amp;','')
urls = 'https://docs.google.com' + url_down
print urls
res = s.get(urls,headers=headers, stream=True)
start = time.time()
filename = '/users/qiyue/myxuni/pngtree/obb_download/' + str(int(time.time())) +'.zip'
print filename
# print res.read()
with open(filename, "wb") as code:
    for chunk in res.iter_content(chunk_size=512):
        if chunk:
            code.write(chunk)
# with open(filename, "wb") as code:
#     code.write(res.read())
end = time.time()
print (end - start)
print (741327 % 51245 + 741327 % 913)
#coding:utf8
import requests
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

aaa = requests.get('http://www.jiaoyu123.com/289/289359/').content.decode('gbk')
xml = etree.HTML(aaa)
res = xml.xpath('//div[@id="chapter"]//dd/a/@href')
print res
with open('sss.txt','w+') as f:
    a = 0
    for x in res:
        a += 1
        html = requests.get(x).content.decode('gbk')
        bbb = etree.HTML(html)
        content = bbb.xpath("//div[@id='text_area']//text()")
        ttt = ''
        for y in content:
            y.replace('&nbsp;','')
            ttt += y
            print ttt
        # ttt = unicode(ttt).decode('gbk')
        print a
        f.write(ttt)
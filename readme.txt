1.apkhouse(谷歌云盘)
    http://apkhouse.com/?dl_id=645
    URL:https://docs.google.com/uc?export=download&confirm=q_r9&id=1JQySKZYR8KLRKtcIz7WnzuqezjowQT6k
    get请求,然后再匹配一下类似的URL,其中confirm=q_r9,这4个字母是会变得,连续请求2次,不登录的情况也是可以下载的

2.www101.zippyshare.com
    http://www101.zippyshare.com/v/Iuu4n96Q/file.html
    他的页面有js,计算一下href,拼接成下载地址(必须按照他给的计算,随便蒙的不对)
    document.getElementById('dlbutton').href = "/d/Iuu4n96Q/" + (741327 % 51245 + 741327 % 913) + "/com.gamedevltd.modernstrike.zip";
    拼好后的地址http://www101.zippyshare.com/d/Iuu4n96Q/24781/com.gamedevltd.modernstrike.zip

3.android-1.com
    https://android-1.com/en/file_3305-dw_apk_o.html
    访问页面,匹配链接(正则,也是写在js里的)
    获取https://www.4sync.com/web/directDownload/U13cYaUq/37mzmToo.4331175374f1da932dea415de6b08e15

4.dropapk.com
    https://dropapk.com/11opeywi7z5b
    data = {
        'op':'download2',
        'id':'11opeywi7z5b',
        'rand':'',
        'referer':'https://dropapk.com/11opeywi7z5b',
        'method_free':'Free Download',
        'method_premium':'',
        'adblock_detected':'0',
    }
    根据URL,改一下data里面的id,referer,   post请求,HTML里就有链接
    这个最终的链接是http://server01.dropapk.com:182/d/apc7next4tcdvbi4rgyzhxac2ouhz2v4qpplxuqh3vai7tij7sj4b46ufz3stfforyejojsr/com.blayzegames.iosfps.zip
    d/后面的一长串,是变化的

5.www.dl.farsroid.com    download.directapk.net  URL的结尾是.apk/.zip/.obb的直接下载就可以.
    http://www.dl.farsroid.com/game/Lost-Lands-5-Full-1.0.1(www.Farsroid.com).zip
    http://download.directapk.net/get/2018/01/com.bigfishgames.ritepassageheartstormgoog.zip
    这个直接就能下载

6.apptoko.com
    https://apptoko.com/android/details?id=com.Xiibi.Prince
    用session,他需要cookie
    访问URL,获取一个ID,266485,然后post  https://apptoko.com/android/android/general_download
    post_data = {'version_id':version_id} ID就是匹配下来的
    返回一个json数据,正则匹配出download URL
    http://dl22.sopcast.mobi/download/s/20161007/diUcvmq4izpg0o8sMFRc_g/1516957179/Deiland_1.3.1.apk
    
7.www.directapk.net
    http://www.directapk.net/1Mkr
    使用session,连续请求2次,和谷歌云盘一样的套路.
    请求URL,正则匹配出download URL
    http://www.directapk.net/1Mkr?pt=9Rv%2Bz5WgNGeDz2XV6hFKz5ZCGsUB%2BORpuU4XJCjUjr0%3D

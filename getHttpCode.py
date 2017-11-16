#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import redis
import time

from callsendmail import cls_sendmail

redis_host = 'localhost'
redis_port = '6379'
redis_db = '0'
rs = redis.StrictRedis(host=redis_host,port=redis_port,db=redis_db)

class httpcode():
    def __init__(self,url):
        self.url = url

    def get_code(self):
        print self.url+' status code:',
        return requests.get(self.url).status_code

if __name__ == "__main__":
#redis SADD Serverlist http1 http2 etc.
    urllist = rs.smembers ('Serverlist')
#    urllist = ['http://www.baidu.com','http://www.google.com']
    print urllist
    for url in urllist:
        try:
            url_code = httpcode(url)
            status =  str(url_code.get_code())
        except Exception, e:
            print repr(e)
            print '--try again--'
            time.sleep(1)
            try:
                url_code = httpcode(url)
                status =  str(url_code.get_code())
            except Exception, e:
                print repr(e) + 'Dead'
                status = str('000')

        if status == str(rs.get(url)):
            print 'No change:' + status
        else :
            print 'Change:'+ status + str(rs.set(url,status))
            msg = '<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body>\n<font style="font-family:Microsoft YaHei">\n<br/>Chack Server RepoMail\n<br/>date: '+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+'\n<br/>URL: '+url+'\n<br/>HttpCode: '+status+'\n<br/><HR align=left width=300 color=#987cb9 SIZE=1> </font>  \n</body>\n</html>'
            print cls_sendmail('Status Change repo',msg).sendmail()
            time.sleep(0.5)


    uploadTime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print uploadTime+ " " + str(rs.set('uploadTime',uploadTime))
    print '-----------------------------------------------------'


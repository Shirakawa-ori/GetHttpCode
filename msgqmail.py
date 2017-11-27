#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import redis
import time
import multiprocessing
from callsendmail import cls_sendmail

redis_host = 'localhost'
redis_port = '6379'
redis_db = '0'
rs = redis.StrictRedis(host=redis_host,port=redis_port,db=redis_db)

def smail(msg):
    print cls_sendmail('Status Change repo',msg).sendmail()
def Checkey(key):
    return rs.exists(key)

def readlist(key):
    return rs.smembers (key)

def doit(key):
    print 'smgList is: ' +key + ' @'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    if Checkey(key):
        for url in readlist(key):
            print url
            if url:
                status = str(rs.get(url))
                msg = '<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body>\n<font style="font-family:Microsoft YaHei">\n<br/>Chack Server RepoMail\n<br/>date: '+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+'\n<br/>URL: '+url+'\n<br/>HttpCode: '+status+'\n<br/><HR align=left width=300 color=#987cb9 SIZE=1> </font>  \n</body>\n</html>'
                p = multiprocessing.Process(target = smail, args = (msg,))
                p.start()
                print 'remove list '+str(rs.srem(key,url))
                print 'remove keys '+str(rs.delete(url))
    else:
        print 'list is null'

if __name__ == "__main__":
    while(1):
        doit('smglist')
        time.sleep(1)

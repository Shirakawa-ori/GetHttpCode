#!/usr/bin/python
# -*- coding: UTF-8 -*-
import redis
import sys

redis_host = 'localhost'
redis_port = '6379'
redis_db = '0'
rs = redis.StrictRedis(host=redis_host,port=redis_port,db=redis_db)
rs.delete('Serverlist')

for i in range(1, len(sys.argv)):
    if sys.argv[i] == '':
        print sys.argv[i]+' ,is null'
    elif sys.argv[i] == ' ':
        print sys.argv[i]+' ,is null'
    else :
        print "URL", i, sys.argv[i]
        print rs.sadd('Serverlist',sys.argv[i])
        print 'default Code 200'
        print rs.set(sys.argv[i],'200')

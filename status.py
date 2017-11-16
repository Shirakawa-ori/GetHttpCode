#!/usr/bin/python
#coding=utf-8 
import redis
import random
import time
from wsgiref.simple_server import make_server  

serverport = 8005

redis_host = 'localhost'
redis_port = '6379'
redis_db = '0'
rs = redis.StrictRedis(host=redis_host,port=redis_port,db=redis_db)

html_HEAD = '<html><head><title>StatUS</title></head><body><table border="1">'
html_END = '</table></body></html>'
#rds = 'SERVER1'

def nvisitor():
    visitor = rs.get('visitor')
    if visitor != '':
        try:
            visitor = int(visitor) + 1
        except Exception, e:
            print repr(e)
            rs.set('visitor','0')
        rs.set('visitor',str(visitor))
    else:
        rs.set('visitor','0')
        print 'visitor set 0'
    return visitor

def getstatus():
    try:
        sleepTime = round(random.uniform(0,6),2)
        print sleepTime
        #time.sleep(sleepTime)
        urllist = rs.smembers ('Serverlist')
        print urllist
        uplodaTime = table =tables = ''

        for url in urllist:
            http_code = rs.get(url)
            if http_code != '200':
                http_code = '<font color="#FF0000"><strong>'+http_code+'</strong></font>'
            else:
                http_code = '<font color="#0000FF"><strong>'+http_code+'</strong></font>'
            url = '<a href="'+url+'" target="_blank">' +url+ "</a>"
            table = '<tr><td>'+str(url)+'</td><td>'+str(http_code)+'</td></tr>'
            tables = tables + table
        uplodaTime = '<tr><td>uploadTime</td><td>'+str(rs.get('uploadTime'))+'</td></tr>'+'<tr><td>Current time</td><td>'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+'</td></tr>'
        pv = 'PV : ' + str(nvisitor())
        pv = '<font><strong>'+pv+'</strong></font>'
        repo = html_HEAD + tables + uplodaTime + pv + html_END
        return repo
    except Exception, e:
        print repr(e)
        return 'Server except'
 
def app(environ, start_response):  
    status = "200 OK"
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    # The returned object is going to be printed  
    return getstatus()
  
httpd = make_server('', serverport, app)  
print 'Serving on port '+ str(serverport) +'...'  
  
# Serve until process is killed  
httpd.serve_forever()  

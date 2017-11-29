#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys   
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime
import random

class cls_sendmail:
    def __init__(self,subject,msg):
        self.subject = subject
        self.msg = msg
        
    def sendmail(self):
        try:
            print 'subject:' + self.subject
        except BaseException:
            print "error! need subject!"
            exit(0)

        try:
            print 'mail_smg:' + self.msg
        except BaseException:
            print "error! need smg"
            exit(0)

        randomS = str(random.randint(0, 99))
        print 'Random: ' + randomS

        #SMTP 服务

        mail_host="smtp.******.com"              #smtp服务器
        mail_user="******@******.com"          #user
        mail_pass="*************"               #pwd 
        sender = '*******@*****.com'           #发送邮箱
        receivers = ['********@******.com,******@*****.com']      #接收邮箱

        message = MIMEText("<html>" + self.msg + "</html>", 'html', 'utf-8')
        message['From'] = Header("********@******", 'utf-8')	#发件人
        message['To'] =  Header("********@******", 'utf-8')		#收件人
        subject = self.subject +'_RANDOM_'+randomS
        #subject = '服务不可达报告' 					#主题
        message['Subject'] = Header(subject, 'utf-8')			#正文
        print 'Subject+Random:' + subject
        
        try:
            smtpObj = smtplib.SMTP_SSL() 
            smtpObj.connect(mail_host, 465)					#SMTP端口号
            smtpObj.ehlo()
            smtpObj.login(mail_user,mail_pass)  
            smtpObj.sendmail(sender, receivers, message.as_string())
            smtpObj.close()  
            return ">邮件发送成功"
        except smtplib.SMTPRecipientsRefused:
            return '>邮件发送失败，收件人被拒绝'
        except smtplib.SMTPAuthenticationError:
            return '>邮件发送失败，认证错误'
        except smtplib.SMTPSenderRefused:
            return '>邮件发送失败，发件人被拒绝'
        except smtplib.SMTPException,e:
            return '>邮件发送失败, ', e.message
        print('!' * 20)

if __name__ == "__main__":
    print 'sleep'
    print cls_sendmail('msgtest','testtoo').sendmail()

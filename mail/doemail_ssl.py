#!/usr/bin/env python
#!coding=utf-8
#author=guolin

import time
import sys
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart  
import sys 
reload(sys)
sys.setdefaultencoding( "utf-8")
   
from_addr = 'web@soilove.cn'
password = '123456'
to_addr = 'root@soilove.cn'
smtp_server = 'smtp.soilove.cn'
sslPort= 465
 
def do_send():
    now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print now_time , 'start ...'
    msg = MIMEText('<html><h3>时间：'+''.join(now_time)+'，内容：test</h3></html>','html','utf-8') 
    msg['Subject'] = 'test邮件'
    msg['From'] = from_addr
    msg['To'] = to_addr
    try:
        smtp = smtplib.SMTP_SSL(smtp_server,sslPort) 
        smtp.login(from_addr, password)
        smtp.sendmail(from_addr, [to_addr], msg.as_string())
        smtp.close()
        print now_time , 'end ...'
    except Exception, e:
        print e
    
if __name__=="__main__":
    do_send()    
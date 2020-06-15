#!/usr/bin/env python3    
#coding: utf-8
#author=guolin
 
import time
import smtplib    
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart    
import sys 
reload(sys)
sys.setdefaultencoding( "utf-8")
 
from_addr = 'root@soilove.cn'
password = '1234567'
to_addr = 'guolin@zzz.com'
smtp_server = 'smtp.soilove.cn'

def do_send():
    now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    msg = MIMEText('<html><h3>时间：'+''.join(now_time)+'，内容：服务挂了</h3></html>','html','utf-8') 
    msg['Subject'] = '服务告警邮件'
    msg['From'] = from_addr
    msg['To'] = to_addr
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server)
        smtp.login(from_addr, password)
        smtp.sendmail(from_addr, [to_addr], msg.as_string())
        smtp.close()
    except Exception, e:
        print e
    
if __name__=="__main__":
    do_send() 
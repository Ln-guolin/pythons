#!/usr/bin/env python
#!coding=utf-8
#author=guolin
import os
import time
import sys
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart  
 
def sendWarningEmail (warning):
    
    from_addr = 'web@soilove.cn'
    password = '123456'
    to_addr = 'root@soilove.cn'
    smtp_server = 'smtp.soilove.cn'
 
    now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print now_time , '开始发送邮件'
    msg = MIMEText('<html><h3>时间：'+''.join(now_time)+'，内容：'+''.join(warning)+'</h3></html>','html','utf-8') 
    msg['Subject'] = '服务告警邮件'
    msg['From'] = from_addr
    msg['To'] = to_addr
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server)
        smtp.login(from_addr, password)
        smtp.sendmail(from_addr, [to_addr], msg.as_string())
        smtp.close()
        print now_time , '发送邮件完成'
    except Exception, e:
        print e 
 
while True:
    # 执行命令，查看启动的进程
    lines = os.popen('netstat -tulnp | grep java','r').readlines()
    now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    try:
        if lines == []:
            print now_time , '严重警告！无任何端口开启，不做任何处理，发送紧急邮件处理 ... '
            
        else:
            # 解析进程端口
            ports = []
            for i in range(len(lines)):
                str = ''.join(lines[i])
                port = str.split()[3].split(':')[-1]
                print now_time , '运行中的进程端口：' , port
                # 循环将端口放入数组
                ports.append(port)
       
            # 检测git服务
            if "8081" in ports:
                print now_time , '检测git服务8081端口：正常'
            else:
                print now_time , '检测git服务8081端口：未找到，准备启动服务...'
                os.system('sh /home/sh/gitbucket/start.sh')
                sendWarningEmail(warning = "检测git服务：服务已挂，正在启动")
                
            # 检测disconf分布式配置中心
            if "8015" in ports:
                print now_time , '检测disconf分布式配置中心8015端口：正常'
            else:
                print now_time , '检测disconf分布式配置中心8015端口：未找到，准备启动服务...'
                os.system('sh /home/sh/disconf/start.sh')
                sendWarningEmail(warning = "检测disconf分布式配置中心：服务已挂，正在启动")
            
            # 检测沙果记账服务
            if "8080" in ports:
                print now_time , '检测沙果记账服务8080端口：正常'
            else:
                print now_time , '检测沙果记账服务8080端口：未找到，准备启动服务...'
                os.system('sh /home/sh/cashbook/start.sh')
                sendWarningEmail(warning = "检测沙果记账服务：服务已挂，正在启动")
                
        time.sleep(60)
    except KeyboardInterrupt:
        sys.exit('\n')
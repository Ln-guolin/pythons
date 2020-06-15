#!/usr/bin/env python
#coding=utf-8
#author=guolin
import os
import time
import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import sys 
reload(sys)
sys.setdefaultencoding( "utf-8")  

# 有时候在家里，需要连接公司电脑进行问题处理，但是发现vpn没法用，而远程软件TeamViewer也未开启，懵逼了！
# 所以需要一个手段来远程启动TeamViewer

def get_mail_Subject(msg):
    value = msg.get('Subject', '')
    if value:
        # 需要解码Subject字符串
        value = decode_str(value)
    #print u'Subject:',value
    return value
        
def get_mail_From(msg):
    value = msg.get('From', '')
    if value:
        # 需要解码Email地址
        hdr, addr = parseaddr(value)
        name = decode_str(hdr)
        value = u'%s <%s>' % (name, addr)
    #print u'From:',value
    return value
          
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def getEmail(email,password):
   
    pop3_server = 'pop3.soilove.cn'
     
    # 连接到POP3服务器:
    server = poplib.POP3(pop3_server)
    
    # 身份认证
    server.user(email)
    server.pass_(password)
    
    # list()返回所有邮件的编号
    resp, mails, octets = server.list()
    
    # 获取最新一封邮件, 注意索引号从1开始
    index = len(mails)
    resp, lines, octets = server.retr(index)
    
    # lines存储了邮件的原始文本的每一行,可以获得整个邮件的原始文本
    msg_content = '\r\n'.join(lines)
    
    # 解析出邮件:
    msg = Parser().parsestr(msg_content)
    
    # 邮件的From, Subject
    mail_from = get_mail_From(msg)
    mail_subject = get_mail_Subject(msg)
    
    # 指令判断
    rs = openTvr(mail_from,mail_subject)
    if rs == '1':
        # 根据邮件索引直接从服务器删除邮件
        server.dele(index)
    
    # 关闭连接:
    server.quit()
    

def startCX(email,password):
    # 循环检测邮件，判断是否有来自指定邮件的指定指令，接收到指令，则启动软件
    while True:
        getEmail(email,password)
        # 每60秒执行一次
        time.sleep(60)

def openTvr(mail_from,mail_subject):
    now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if (mail_subject == 'cmd_start_tvr') and ('root@soilove.cn' in mail_from):
        print u'接收邮件指令，准备打开TeamViewer软件:',now_time
        os.startfile("C:\Program Files (x86)\TeamViewer\TeamViewer.exe")
        return '1'
    else:
        print u'接收邮件指令，不进行任何处理:',mail_from,mail_subject,now_time
        return '0'
        
if __name__ == '__main__':
    # 输入邮件地址, 口令和POP3服务器地址:
    #email = raw_input(u'请输入妈妈好邮箱账户: '.decode('utf-8').encode('gbk'))
    #password = raw_input(u'请输入妈妈好邮箱密码: '.decode('utf-8').encode('gbk'))
    email = "web@soilove.cn"
    password = "123456"
    
    startCX(email,password) 
    
            

    
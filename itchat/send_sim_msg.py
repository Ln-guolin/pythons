#!/usr/bin/env python
#!coding=utf-8
import itchat
import datetime, os, platform,time
import sys
reload(sys)
sys.setdefaultencoding( "utf-8")

def timerfun(sched_time) :
    flag = 0
    while True:
        now = datetime.datetime.now()
        if now > sched_time and now < sched_time + datetime.timedelta(seconds=1) :  # 因为时间秒之后的小数部分不一定相等，要标记一个范围判断
            send_move()
            time.sleep(1)    # 每次判断间隔1s，避免多次触发事件
            flag = 1
        else :
            #print('schedual time is {0}'.format(sched_time))
            #print('now is {0}'.format(now))
            if flag == 1 :
                sched_time = sched_time + datetime.timedelta(hours=1)  # 把目标时间增加一个小时，一个小时后触发再次执行
                flag = 0

def send_move():
    users = itchat.search_friends(name=u'媳妇')   # 使用备注名来查找实际用户名
    #获取好友全部信息,返回一个列表,列表内是一个字典
    print(users)
    #获取`UserName`,用于发送消息
    userName = users[0]['UserName']
    itchat.send(u'测试发送消息！',toUserName = userName)
    print('succeed')

if __name__=='__main__':
    itchat.auto_login()  # 首次扫描登录后后续自动登录
    send_move()
    #sched_time = datetime.datetime(2017,11,6,16,24,10)   #设定初次触发事件的事件点
    #print('run the timer task at {0}'.format(sched_time))
    #timerfun(sched_time)
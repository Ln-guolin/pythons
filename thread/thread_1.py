#!/usr/bin/env python
#coding=utf-8
#author=guolin
#使用thread模块创建线程
import thread
import time
import sys 
reload(sys)
sys.setdefaultencoding( "utf-8")
 
def calc(name):
    now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print  u'用户=',name,u'时间=',now_time
    time.sleep(5)  
 

if __name__ == '__main__':
    try:
       # 开新线程去执行calc函数
       thread.start_new_thread( calc, (u"张三",) )
       thread.start_new_thread( calc, (u"李四",) )
       thread.start_new_thread( calc, (u"王五",) )
    except:
       print "Error: start thread error"
       
    # 主线程不能停，否则新线程起不来，呵呵   
    while 1:
        pass
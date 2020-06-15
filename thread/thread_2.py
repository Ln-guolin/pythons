#!/usr/bin/env python
#coding=utf-8
#author=guolin
#使用Threading模块创建线程
import threading
import time
import sys 
reload(sys)
sys.setdefaultencoding( "utf-8")

# 线程锁，用于同步执行的时候
threadLock = threading.Lock()
num = 5
 
class myThread (threading.Thread):# 继承父类 threading.Thread
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        
    def run(self):   
        # 要处理的内容
        calc(self.name)
        
        # 开启锁
        threadLock.acquire()
        # 要同步处理的内容
        calc_num(self.name)
        # 释放锁
        threadLock.release()
 
def calc(name):
    now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print  u'用户=',name,u'时间=',now_time
    time.sleep(2) 
 
def calc_num(name):
    # 全局变量
    global num
    
    now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print  u'不能并发，用户=',name,u' num=',num,u'时间=',now_time
    num = num - 1
    time.sleep(1)
    
if __name__ == '__main__':
    
    # 创建线程去执行calc函数
    thread1 = myThread(u"zhangsan")
    thread2 = myThread(u"lisi")
     
    # 开启新线程
    thread1.start()
    thread2.start()
#!/usr/bin/env python
#!coding=utf-8
#author=guolin
import sys
reload(sys)
sys.setdefaultencoding( "utf-8")

# 编译文件存放路径
file_path = u"/tmp/arthas";
# 方法的reference路径，只需替换这个即可
reference_path = u"com.yueshuang.uc.web.controller.admin.vote.AdminVoteActivityController#activityList";

if __name__=="__main__":

    print u'######生成trace方法请求链路监测命令######'
    print u'trace 能方便的帮助你定位和发现因 RT 高而导致的性能问题缺陷，但每次只能跟踪一级方法的调用链路'
    print u'注：以下命令按"q"退出'

    methodName = reference_path.split('#')[-1]
    classPath = reference_path.split('#')[0]

    print u'\n1,监控方法的请求链路以及耗时，次数=3，耗时>1毫秒：'
    print 'trace '+classPath+' '+methodName+' -n 3 "#cost>1"'


    print u'\n2,将jdk函数执行过程也收集出来：'
    print 'trace --skipJDKMethod false '+classPath+' '+methodName+' -n 3 "#cost>1"'

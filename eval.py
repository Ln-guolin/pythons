#!/usr/bin/env python
#coding=utf-8
import thread
import time
import sys 
reload(sys)
sys.setdefaultencoding( "utf-8")
 
def calc():
    num = eval('3+6/(3-2)*3')
    print num


if __name__ == '__main__':
   
    calc()
    
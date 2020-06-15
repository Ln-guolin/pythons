#!/usr/bin/env python
# coding=utf-8
# author=guolin
import time
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def get_timestamp_10_len():
    t = time.time()
    return unicode(int(t))

def get_timestamp_13_len():
    t = time.time()
    return unicode(int(round(t*1000)))

if __name__=="__main__":

    print u"10位时间戳=" + get_timestamp_10_len()
    print u"13位时间戳=" + get_timestamp_13_len()
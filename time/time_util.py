#!/usr/bin/env python
# coding=utf-8
# author=guolin
import time
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
from datetime import datetime

def get_timestamp_10_len():
    t = time.time()
    return unicode(int(t))

def get_timestamp_13_len():
    t = time.time()
    return unicode(int(round(t*1000)))

def parseDate(text):

   if "-" in text:
       return datetime.strptime(text, "%Y-%m-%d").date()
   elif "/" in text:
       return datetime.strptime(text, "%Y/%m/%d").date()
   else:
       print(u"日期转换异常：",text)
       return None

def times_days(date,num):
    import datetime
    # 计算偏移量:days,hours,minutes,seconds
    offset = datetime.timedelta(days=num)
    # 获取修改后的时间并格式化
    re_date = (date + offset).strftime('%Y-%m-%d')
    return re_date

if __name__=="__main__":

    print u"10位时间戳=" + get_timestamp_10_len()
    print u"13位时间戳=" + get_timestamp_13_len()
    text = '2018-11-21'
    a = parseDate(text)

    c = 5
    for count in range(0, c):
        d = times_days(a,+count)
        print d
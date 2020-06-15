#!/usr/bin/env python
#coding=utf-8
#author=guolin
import  md5
import sys
reload(sys)
sys.setdefaultencoding( "utf-8")

# md5加密，小写--32
def md5_32_toLowerCase(str):
    md5_str = md5.new(str).hexdigest()

    print u'加密后的字符：',md5_str
    return md5_str

# md5加密，大写--32
def md5_32_toUpperCase(str):
    md5_str = md5.new(str).hexdigest().upper()

    print u'加密后的字符：',md5_str
    return md5_str

if __name__=="__main__":
    str = "测试abc123"
    md5_32_toLowerCase(str)
    md5_32_toUpperCase(str)
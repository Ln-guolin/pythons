#!/usr/bin/env python
#coding=utf-8
#author=guolin
import base64
import sys
reload(sys)
sys.setdefaultencoding( "utf-8")

# base64加密 -- utf-8
def b64encode_utf8(str):
    encoded = base64.b64encode(str.encode(encoding='utf-8'))
    print u'加密后的字符(utf-8)：',encoded
    return encoded

# base64加密
def b64encode(str):
    encoded = base64.b64encode(str)
    print u'加密后的字符：',encoded
    return encoded

# base64解密
def b64decode(str_base64):
    encoded = base64.b64decode(str_base64)
    print u'解密后的字符：',encoded
    return encoded

if __name__=="__main__":
    str = "测试abc123"
    str_base64 = b64encode(str)
    b64decode(str_base64)

    str_base64_2 = b64encode_utf8(str)
    b64decode(str_base64_2)
#!/usr/bin/env python
#!coding=utf-8
#author=guolin
import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8")

# 字符串转json对象
def str2json(str):
    result = json.loads(str)
    print u'转换后的json对象=',result
    return result

# json对象转字符串
def json2str(str_json):
    result = json.dumps(str_json)
    print u'转换后的字符串=',result
    return result


if __name__=="__main__":
    str = '{"name":"zhangsan"}'
    result_json = str2json(str)

    str_json = {"name":"zhangsan"}
    json2str(str_json)
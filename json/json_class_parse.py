#!/usr/bin/env python
#!coding=utf-8
#author=guolin
import sys
reload(sys)
import json
sys.setdefaultencoding( "utf-8")

### class , json , json字符串 互转

class User:
    code = ""
    name = ""

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def print_str(self):
        print "-----------------------------------"
        print u"code=" + unicode(self.code)
        print u"name=" + unicode(self.name)
        print "-----------------------------------"

if __name__=="__main__":

    print u'开始脚本...'

    user = User("123",u"lisi")
    user.print_str()

    # class 转 json 字符串
    json_str = json.dumps(user, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
    print json_str

    # json 字符串 转 json
    json_obj = json.loads(json_str)
    print json_obj["name"]

    # json 字符串 转 class
    def dict2user(d):
        return User(d['code'], d['name'])
    tmp_user = json.loads(json_str, object_hook=dict2user)
    print tmp_user.name

    print u'执行完成！'




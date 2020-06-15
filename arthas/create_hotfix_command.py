#!/usr/bin/env python
#!coding=utf-8
#author=guolin
import sys
reload(sys)
sys.setdefaultencoding( "utf-8")

# 编译文件存放路径
file_path = u"/tmp/arthas";
# 类reference路径，只需替换这个即可
reference_path = u"com.yueshuang.uc.web.config.AdminLoginInterceptor";

if __name__=="__main__":

    print u'######生成热更新命令######'

    print u'\n1,把class反编译为java类：'
    print 'jad --source-only '+reference_path+' > '+file_path+'/'+reference_path.split('.')[-1]+'.java'

    print u'\n2,修改java类，并重新编译为class：'
    print 'mc -d '+file_path+' '+file_path+'/'+reference_path.split('.')[-1]+'.java'

    print u'\n3,获取类的classLoaderHash：'
    print 'sc -d *'+reference_path.split('.')[-1]

    print u'\n4,将class热更到jvm中：'
    print u'redefine -c 【替换为classLoaderHash】 '+file_path+'/'+reference_path.replace('.','/')+'.class'

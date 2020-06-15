#!/usr/bin/env python
#!coding=utf-8
#author=guolin
import sys
reload(sys)
sys.setdefaultencoding( "utf-8")

# 编译文件存放路径
file_path = u"/tmp/arthas";
# 方法的reference路径，只需替换这个即可
reference_path = u"com.yueshuang.uc.web.controller.h5.settle.UserOrderController#order";

if __name__=="__main__":

    print u'######生成方法监测命令tt和watch######'
    print u'注：以下命令按"q"退出'

    methodName = reference_path.split('#')[-1]
    classPath = reference_path.split('#')[0]

    print u'\n1,使用watch命令观察到方法的参数、返回和异常情况，深度=3、次数=3：'
    print 'watch '+classPath+' '+methodName+' "{params,returnObj,throwExp}" -x 3 -n 3'

    print u'\n2,将观察记录到本地文件中：'
    print 'watch '+classPath+' '+methodName+' "{params,returnObj,throwExp}" -x 3 -n 10 > '+file_path+'/watch.log &'

    print u'\n3,只观察异常的请求：'
    print 'watch '+classPath+' '+methodName+' "{params,returnObj,throwExp}" -x 3 -n 3 -e'

    print u'\n4,只观察大于200毫秒的请求：'
    print 'watch '+classPath+' '+methodName+' "{params,returnObj,throwExp}" -x 3 -n 3 "#cost>200"'

    print u'\n5,观察请求方法对象，使用类似target.user形式的命令查看对象：'
    print 'watch '+classPath+' '+methodName+' -n 3 "target"'

    print u'\n6,使用tt命令记录下方法的每次调用环境现场，次数=20：'
    print 'tt -t -n 20 '+classPath+' '+methodName

    print u'\n7,使用tt -l可以查看记录的列表：'
    print 'tt -l'

    print u'\n8,使用tt -i index查看调用信息：'
    print 'tt -i [替换为INDEX]'

    print u'\n9,使用tt -i index -p重新发起一次请求：'
    print 'tt -i [替换为INDEX] -p'

    print u"\n10,使用tt -i index -w 'target'查看对象信息，也使用类似target.user形式的命令查看对象："
    print "tt -i [替换为INDEX] -w 'target'"



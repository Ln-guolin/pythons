#!/usr/bin/env python
#!coding=utf-8
#author=guolin
import sys
reload(sys)
import os
sys.setdefaultencoding( "utf-8")

# 文件路径
file_path = r"/tmp/uc/download/";

os_path = os.walk(file_path)

# 读取文件夹下的文件列表
def calc():
    for path,dir_list,file_list in os_path:
        for file_name in file_list:
            filename = os.path.join(path, file_name)
            print u'读取到文件：'+filename

if __name__=="__main__":
    print u'开始处理...'
    calc()
    print u'处理完成！'



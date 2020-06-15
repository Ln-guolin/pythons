#!/usr/bin/env python3    
#coding: utf-8
#author=guolin
   
import sys 
reload(sys)
sys.setdefaultencoding( "utf-8")

# 新建文本 \n 表示换行
def txt_w():
    with open("D:\Python27\py\pytest.txt","w") as f:
        f.write("12345qweqwe\n")

# 追加文本
def txt_a():        
    with open("D:\Python27\py\pytest.txt","a") as f:
        f.write("12345qweqwe\n")
    
# 读取文本    
def txt_read():    
    
    print("start read txt")
    nos = []
    file = open("D:\Python27\py\data.txt")
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        nos.append(line)
    print "start read txt end"

if __name__=="__main__":
    txt_w()     
#!/usr/bin/env python
#!coding=utf-8
#author=guolin
import xlrd
import sys
reload(sys)
sys.setdefaultencoding( "utf-8")


def calc(file_path,save_path):

    # 打开文件
    book = xlrd.open_workbook(file_path)

    # 通过名称获取sheet对象
    #sheet=book.sheet_by_name(u'市')
    # 通过索引数获取sheet对象
    sheet=book.sheet_by_index(0)

    # 获取行数和列数
    print u'总行数：' , sheet.nrows,u'，总列数：' , sheet.ncols

    # 遍历所有行
    n = 0
    result= []
    for i in range(1,sheet.nrows):
        n = n + 1
        hang = sheet.row_values(i)
        term = get_name(n,hang[0],hang[1])
        result.append(term)
    print u'排序，总数据条数：',n
    result.sort()
    with open(save_path,"w") as f:
        f.writelines(result)
    print u'数据已经保存到：',save_path

def get_name(n,num,num2):
    return str(str(num)).replace(" ", "")+"#"+str(str(num2)).replace(" ", "")+"\n"


file_path1 = r"/Users/apple/Desktop/uc/ucuser.xlsx";
file_path2 = r"/Users/apple/Desktop/uc/mruser.xlsx";

save_path1="/Users/apple/Desktop/uc/ucuser.txt"
save_path2="/Users/apple/Desktop/uc/mruser.txt"

if __name__=="__main__":

    calc(file_path1,save_path1)
    calc(file_path2,save_path2)
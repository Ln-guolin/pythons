#!/usr/bin/env python
#!coding=utf-8
#author=guolin
import xlrd  
import sys 
reload(sys)
sys.setdefaultencoding( "utf-8")
 
def openfile():
 
    # 打开文件  
    book = xlrd.open_workbook(r'f:citys.xlsx') 
      
    # 获取sheet对象名称  
    sheet_str = u'sheet对象名称:'
    for i in range(len(book.sheet_names())):
        sheet_str += book.sheet_names()[i] + ','
    print sheet_str
 
 
    # 通过名称获取sheet对象 
    sheet=book.sheet_by_name(u'市') 
    # 通过索引数获取sheet对象  
    #sheet=book.sheet_by_index(0)    
      
    # 获取行数和列数  
    print u'总行数：' , sheet.nrows,u'，总列数：' , sheet.ncols
 
    # 获取指定行指定列的值
    print u'获取第1行第1列的值：',sheet.cell_value(0,0)  
 
    # 遍历所有行
    for i in range(0,sheet.nrows):
        print u'遍历所有行，索引：',i,u'行内容:',sheet.row_values(i)
 
    # 遍历所有列
    for i in range(0,sheet.ncols):
        print u'遍历所有列，索引：',i,u'列内容:',sheet.col_values(i)
 
 
if __name__=="__main__":
    openfile()    
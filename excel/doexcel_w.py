#!/usr/bin/env python
#!coding=utf-8
#author=guolin
import xlwt
from datetime import datetime
 
def writefile():
    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 2
    font0.bold = True
      
    style0 = xlwt.XFStyle()
    style0.font = font0
      
    style1 = xlwt.XFStyle()
    style1.num_format_str = 'D-MMM-YY'
    
    # 创建文档对象
    wb = xlwt.Workbook()
    
    # sheet表名称
    ws = wb.add_sheet('A Test Sheet')
    
    # 行，列，值
    ws.write(0, 0, 'Test', style0)
    ws.write(1, 0, datetime.now(), style1)
    ws.write(2, 0, 1)
    ws.write(2, 1, 1)
    ws.write(2, 2, xlwt.Formula("A3+B3"))
    
    # 文件写入路径    
    wb.save('f://example1.xls')
 
if __name__=="__main__":
    writefile()
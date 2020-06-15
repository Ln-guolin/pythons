#!/usr/bin/env python
#!coding=utf-8
#author=guolin
import sys
reload(sys)
import os
import xlrd
import xlwt
sys.setdefaultencoding( "utf-8")
# excel合并处理，拷贝多个excel的数据合并到一个Excel中

# 合并后的文件路径
save_excel_path = r"/Users/chenguolin/Downloads/settle_merge_calc.xls";
# 需要合并的excel文件夹路径
os_path = os.walk(r"/tmp/uc/download/")

# 列数
col_num = 16
title_num = 0
hang_title = []
hangs = []

# 读取文件夹路径的文件列表
def calc():
    for path,dir_list,file_list in os_path:
        for file_name in file_list:
            filename = os.path.join(path, file_name)
            print u'读取到文件：'+filename
            suffix = filename.split('.')[-1]
            if suffix == 'xlsx':
                print u'开始处理文件：'+filename
                openExcel(filename)

def openExcel(path):
    book = xlrd.open_workbook(unicode(path))
    sheet = book.sheet_by_index(0)

    # 表头
    for i in range(0,sheet.nrows):
        global title_num
        if title_num == 0:
            hang_title.append(sheet.row_values(i))
            title_num = title_num + 1

    # 表体
    for i in range(1,sheet.nrows):
        hangs.append(sheet.row_values(i))

def saveExcel():
    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 2
    font0.bold = True

    style0 = xlwt.XFStyle()
    style0.font = font0

    # 创建文档对象
    wb = xlwt.Workbook()

    # sheet表名称
    ws = wb.add_sheet(u'自定义sheet名称')

    # ws.write 行，列，值

    # 表头处理
    for num in range(0,col_num + 1):
        ws.write(0, num, unicode(hang_title[0][num]),style0)

    # 定义行号
    row = 1
    # 遍历读取数据
    for hang in hangs:
        # excel最大行数
        excel_max_row = unicode(len(hangs))
        # 当前行>最大行时，停止
        if row > excel_max_row:
            print u'遍历完成，停止！'
            return

        # 写入表体数据
        try:
            for num in range(0,col_num + 1):
                ws.write(row, num, unicode(hang[num]))
        except Exception as e:
            print u'#发生异常，用户code=',hang[0],'，跳过：' ,e

        # 设置下一行
        row = row + 1

    # 文件写入路径
    wb.save(save_excel_path)

if __name__=="__main__":
    print u'开始处理...'
    calc()
    saveExcel()
    print u'处理完成！文件已保存到：'+save_excel_path



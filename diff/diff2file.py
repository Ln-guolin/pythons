#!/usr/bin/env python
#!coding=utf-8
#author=guolin
import sys
reload(sys)
sys.setdefaultencoding( "utf-8")

import difflib

def diff(file_path_1, file_path_2, report_html_path):
    txt_line1 = get_lines(file_path_1)
    txt_line2 = get_lines(file_path_2)

    d = difflib.HtmlDiff()

    fid = open(report_html_path, 'w')

    fid.write(d.make_file(txt_line1, txt_line2))

    fid.close()


def get_lines(file_name):
    return open(file_name).readlines()


file_path_1="/Users/apple/Desktop/uc/ucuser.txt"
file_path_2="/Users/apple/Desktop/uc/mruser.txt"
report_html_path="/Users/apple/Desktop/uc/diff.html"


if __name__=="__main__":

    diff(file_path_1, file_path_2, report_html_path)
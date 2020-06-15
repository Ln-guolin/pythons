#!/usr/bin/env python
#coding=gbk
#author=guolin
# py3.7
import ciyun_util

if __name__=="__main__":

    # 自定义去除词库
    remove_words = [u'没有', u'还有', u'时候', u'大家']

    ciyun_util.create(r'./article.txt',r'./bg.jpeg',r'./download.png',remove_words)
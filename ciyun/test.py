#!/usr/bin/env python
#coding=gbk
#author=guolin
# py3.7
import ciyun_util

if __name__=="__main__":

    # �Զ���ȥ���ʿ�
    remove_words = [u'û��', u'����', u'ʱ��', u'���']

    ciyun_util.create(r'./article.txt',r'./bg.jpeg',r'./download.png',remove_words)
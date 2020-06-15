#!/usr/bin/env python
#coding=gbk
#author=guolin
# py3.7
import io
import re
import jieba.analyse
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator

# 结巴分词，创建词云
# data_file_path=数据文件路径
# bg_img_path = 词云背景图片
# new_img_path = 生成的图片路径
# remove_words = 需要移除的关键词，如：[u'没有', u'还有', u'时候']
def create(data_file_path,bg_img_path,new_img_path,remove_words):
    # 读取文件
    fn = io.open(data_file_path,'r',encoding="utf-16")
    txt = fn.read()
    fn.close()

    # 正则表达式去除不需要的字符
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')
    txt = re.sub(pattern, '', txt)

    result = jieba.analyse.textrank(txt,topK=250,withWeight=True)

    # 将需要生成词云的数据放到dict中
    keyworlds = dict()
    for i in result:
        if i[0] not in remove_words:
            keyworlds[i[0]]=i[1]

    # 设置背景图
    graph = np.array(Image.open(bg_img_path))
    # 设置字体，背景色，字体大小等
    wc = WordCloud(font_path='simhei.ttf',background_color='White',max_font_size=170,mask=graph)
    # 词云生成
    wc.generate_from_frequencies(keyworlds)
    # 定义颜色模式，显示图片
    plt.imshow(wc.recolor(color_func=ImageColorGenerator(graph)))
    plt.axis('off')
    plt.show()
    # 生成图片到当前目录
    wc.to_file(new_img_path)
    # 退出程序
    quit()
    print "success! image path = " + unicode(new_img_path)

if __name__=="__main__":

    # 自定义去除词库
    remove_words = [u'没有', u'还有', u'时候', u'大家']

    create('./article.txt','./bg.jpeg','./download.png',remove_words)
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

# ��ͷִʣ���������
# data_file_path=�����ļ�·��
# bg_img_path = ���Ʊ���ͼƬ
# new_img_path = ���ɵ�ͼƬ·��
# remove_words = ��Ҫ�Ƴ��Ĺؼ��ʣ��磺[u'û��', u'����', u'ʱ��']
def create(data_file_path,bg_img_path,new_img_path,remove_words):
    # ��ȡ�ļ�
    fn = io.open(data_file_path,'r',encoding="utf-16")
    txt = fn.read()
    fn.close()

    # ������ʽȥ������Ҫ���ַ�
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')
    txt = re.sub(pattern, '', txt)

    result = jieba.analyse.textrank(txt,topK=250,withWeight=True)

    # ����Ҫ���ɴ��Ƶ����ݷŵ�dict��
    keyworlds = dict()
    for i in result:
        if i[0] not in remove_words:
            keyworlds[i[0]]=i[1]

    # ���ñ���ͼ
    graph = np.array(Image.open(bg_img_path))
    # �������壬����ɫ�������С��
    wc = WordCloud(font_path='simhei.ttf',background_color='White',max_font_size=170,mask=graph)
    # ��������
    wc.generate_from_frequencies(keyworlds)
    # ������ɫģʽ����ʾͼƬ
    plt.imshow(wc.recolor(color_func=ImageColorGenerator(graph)))
    plt.axis('off')
    plt.show()
    # ����ͼƬ����ǰĿ¼
    wc.to_file(new_img_path)
    # �˳�����
    quit()
    print "success! image path = " + unicode(new_img_path)

if __name__=="__main__":

    # �Զ���ȥ���ʿ�
    remove_words = [u'û��', u'����', u'ʱ��', u'���']

    create('./article.txt','./bg.jpeg','./download.png',remove_words)
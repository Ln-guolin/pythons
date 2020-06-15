#!/usr/bin/env python
#coding=utf-8
#author=guolin
#爬图片
import urllib,requests
import os
from bs4 import BeautifulSoup

# 全局变量，统计最后下载数量使用
num = 0

# 设置头部信息
headers = {'referer': 'http://jandan.net/', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}

# 保存图片
def save_pic(res_url):
    # 告诉python这是全局变量
    global num
    # 获得页面
    html = BeautifulSoup(requests.get(res_url, headers=headers).text)
    # 获取所有a标签
    alinks = html.find_all('a', {'class': 'view_img_link'})
    # 循环下载
    for link in alinks:
        num += 1
        # 图片路径
        path = "http:" + link.get('href')
        print("正在下载%s条数据，path=%s" % (num,path))
        # 本地文件路径
        localurl = 'data/{0}.jpg'.format(num)
        # 执行下载
        urllib.request.urlretrieve( path, localurl)


# 抓取煎蛋图片
if __name__ == '__main__':
    # 请求地址
    url = 'http://jandan.net/ooxx'
    # 创建目录保存文件
    ospath = "data"
    if not os.path.exists(ospath):
        os.makedirs(ospath)
    # 抓取2页
    for i in range(1, 2):
        print("页=======================",i)
        # 下载此页面的图片
        save_pic(url)
        # 根据a标签class=previous-comment-page获取href得到下一页
        url = "http:" + BeautifulSoup(requests.get(url, headers=headers).text).find('a', {'class': 'previous-comment-page'}).get('href')
    print("执行完成！")
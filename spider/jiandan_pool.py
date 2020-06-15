#!/usr/bin/env python
#coding=utf-8
#author=guolin
#爬图片-多进程下载
import urllib,requests
import os
from bs4 import BeautifulSoup
from multiprocessing import Pool

# 全局变量，统计最后下载数量使用
num = 0

# 设置头部信息
headers = {'referer': 'http://jandan.net/', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}

# 保存图片路径
def get_pic_path(picpaths,res_url):
    # 获得页面
    html = BeautifulSoup(requests.get(res_url, headers=headers).text)
    # 获取所有a标签
    alinks = html.find_all('a', {'class': 'view_img_link'})
    # 循环下载
    for link in alinks:
        # 图片路径
        path = "http:" + link.get('href')
        picpaths.append(path)
# 下载图片
def down_pic(path,num):
    print("正在下载数据，path=%s" % (path))
    # 本地文件路径
    localurl = 'data/{0}.jpg'.format(num)
    # 执行下载
    urllib.request.urlretrieve( path, localurl)

# 多进程下载图片
def save_pic_pool(picpaths, processes=10):
    print("启动",processes,"个线程下载")
    global num
    pool = Pool(processes)
    for pic in picpaths:
        num += 1
        pool.apply_async(down_pic, (pic,num ))
    pool.close()
    pool.join()


# 抓取煎蛋图片
if __name__ == '__main__':
    # 请求地址
    url = 'http://jandan.net/ooxx'
    # 创建目录保存文件
    ospath = "data"
    # 创建数组存放图片路径
    picpaths = []
    if not os.path.exists(ospath):
        os.makedirs(ospath)

    # 抓取2页
    for i in range(1, 2):
        print("页=======================",i)
        # 下载此页面的图片
        get_pic_path(picpaths,url)
        # 根据a标签class=previous-comment-page获取href得到下一页
        url = "http:" + BeautifulSoup(requests.get(url, headers=headers).text).find('a', {'class': 'previous-comment-page'}).get('href')

    # 开3个线程去执行下载
    save_pic_pool(picpaths,3)
    print("执行完成！")
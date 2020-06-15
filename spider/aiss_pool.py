#!/usr/bin/env python
#coding=utf-8
#author=guolin
#爬图片-通过接口post获取
import requests,urllib
import json
import os


# 请求接口保存返回json
def post_ifc_save_result_json(page):
    # 请求接口获取数据
    url = 'http://api.pmkoo.cn/aiss/suite/suiteList.do'
    params = {
        'page': page,
        'userId': 1
    }
    rsp_json = requests.post(url, data=params).json()
    # 非有效数据移除
    if not rsp_json['data']['list']:
        return
    print("正在保存第",page,"页json数据...")
    # 将json对象转换为字符，存放到本地文件中
    txt = json.dumps(rsp_json)
    with open('data/json.txt', 'a') as f:
        f.write(txt)
        f.write('\n')

# 读取本地文件，开始下载
def get_json_file_download():
    #  逐条读取
    res = []
    with open('data/json.txt', 'r') as f:
        for line in f:
            data = json.loads(line)
            # list是多条数据，所以extend最加多条数据
            res.extend(data['data']['list'])

    #  逐条下载
    for item in res:
        nickname = item["author"]["nickname"]
        catalog = item["source"]["catalog"]
        name = item["source"]["name"]
        issue = item["issue"]
        pictureCount = item["pictureCount"]
        for pic_idx in range(pictureCount):
            # 图片地址
            pic_path = "http://tuigirl-1254818389.cosbj.myqcloud.com/picture/%s/%s/%s.jpg" % (catalog, issue, pic_idx)
            # 本地文件夹
            directory = os.path.join("data", name, "%s" % ( nickname))
            if not os.path.exists(directory):
                os.makedirs(directory)
            # 图片本地路径
            localurl = os.path.join(directory, "%s.jpg" % pic_idx)
            print("正在下载数据，path=%s" % (pic_path))
            # 执行下载，法律原因不可用
            #urllib.request.urlretrieve( pic_path, localurl)
            # 执行下载
            rsp = requests.get(pic_path)
            with open(localurl, 'wb') as f:
                f.write(rsp.content)
                print('已经保存到：', localurl)


if __name__ == "__main__":
    # 初始化文件夹
    directory = os.path.join("data")
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 初始化文件
    with open("data/json.txt","w") as f:
        f.write("")
    # 抓取2页
    for i in range(1, 2):
        post_ifc_save_result_json(i)
    # 下载文件
    get_json_file_download()
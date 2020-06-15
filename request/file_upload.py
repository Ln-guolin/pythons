#!/usr/bin/env python
#!coding=utf-8
#author=guolin
import sys
reload(sys)
import requests
from uuid import uuid4
sys.setdefaultencoding( "utf-8")

# 上传文件

# 环境
profile_url = "http://xxx.cn"

# 下载接口
apiurl = profile_url + "/api/admin/upload/oss"


token = "TMXaYwdA2gWh6PV1dZ62reJBcsrLA-BVw"

paths = []

# pos请求
def req_post(path):
    # 随机uuid
    boundary = uuid4().hex

    # 文件内容
    file_content = get_file_content(path)

    # 头部信息
    headers = {'Content-Type': 'multipart/form-data; boundary={0}'.format(boundary), 'charset': 'UTF-8',"token":token}

    # 文件内容
    datas = '--{0}{1}Content-Disposition: form-data; name="file"; filename="{2}"{1}Content-Type: application/octet-stream{1}{1}{3}{1}--{0}--{1}'. \
        format(boundary, '\r\n', path, file_content, boundary)

    # 发送请求
    r = requests.post(url = apiurl,data=datas,headers = headers)

    # 响应信息
    print u'【'+path+'】上传结果='+r.text

# 获取文件信息
def get_file_content(path):
    with open(path.decode('utf8'), 'r') as f:
        content=f.readlines()
        content=''.join(content)
        return content
    return None

if __name__=="__main__":
    print u'设置上传文件'
    paths.append(r"/Users/chenguolin/Desktop/uc.png")

    print u'开始上传'
    for path in paths:
        req_post(path)
    print u'完成！'



#!/usr/bin/env python
#!coding=utf-8
#author=guolin
#依赖：pip install Pillow
from PIL import Image
import os

# 尺寸比例
size_ratio = 0.3
# 压缩质量
quality = 50

# 遍历文件夹压缩
def batch_compress(srcPath, distPath):

    # 遍历文件夹
    for filename in os.listdir(srcPath):
        # 目录验证
        if not os.path.exists(distPath):
            os.makedirs(distPath)

        # 拼接完整的文件或文件夹路径
        srcFile = os.path.join(srcPath, filename)
        distFile = os.path.join(distPath, filename)

        # 如果是文件 就调用压缩
        if os.path.isfile(srcFile):
            if(is_image(srcFile)):
                # 执行压缩操作
                compression(srcFile,distFile)
            else:
                print (distFile + " 文件不是图片，跳过！")
        # 如果是文件夹 就继续递归
        elif os.path.isdir(srcFile):
            batch_compress(srcFile, distFile)

# 文件是否为图片判断
def is_image(srcFile):
    if (srcFile.lower().endswith(('.bmp', '.dib','.gif', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff'))):
        return True
    else:
        return False

# 压缩图片并保存
def compression(srcFile,distFile):
    try:
        # 读取原图
        srcImg = Image.open(srcFile)
        w, h = srcImg.size
        # 重新设置图片尺寸和选项，Image.ANTIALIAS：平滑抗锯齿
        distImg = srcImg.resize((int(w * size_ratio), int(h * size_ratio)), Image.ANTIALIAS)
        # 保存为新图
        distImg.save(distFile, quality=quality)
        print (distFile + " 压缩成功！")
    except Exception as e:
        print (distFile + " 压缩失败！异常信息：", e)

if __name__ == '__main__':
    print ("=================开始执行=================")
    # 指定图片目录以及压缩后的图片目录
    batch_compress("/Users/mac/Downloads/images", "/Users/mac/Downloads/images/dist")
    print ("=================执行结束=================")
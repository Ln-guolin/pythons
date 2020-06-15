#!/usr/bin/env python
#coding=utf-8
#author=guolin

from selenium import webdriver
import pytesseract
from PIL import Image
import time
import sys
reload(sys)
sys.setdefaultencoding( "utf-8")

# tessdata库：https://github.com/tesseract-ocr/tessdata/

# 指定tesseract命令工具地址
pytesseract.pytesseract.tesseract_cmd = 'D:/Program Files (x86)/Tesseract-OCR/tesseract'
# google浏览器驱动文件chromedriver.exe地址
hromedriver_exe_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

# 网站登录信息
login_url = 'http://yy.xxxx.com/login.do'
login_name = 'guolin'
login_pwd = 'xxxx'

# 网站截图保存地址
screenshot_path = 'f://www.png'
# 网站验证码截图保存地址
screenshot_path_bcode = 'f://www_bcode.png'
# 转化为灰度图的验证效果保存地址
bcode1_calc = 'f://bcode1_calc.png'


# 识别图片文字
def calc_bcode(image):
    # 二值化变量信息准备
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    # 转化到灰度图
    image = image.convert('L')
    # 二值化，采用阈值分割法，threshold为分割点
    image = image.point(table,'1')
    # 保存转化后的图，方便我们查看效果
    image.save(bcode1_calc)
    # 识别为文字
    vcode = pytesseract.image_to_string(image,lang="chi_sim")
    print u'识别出来的内容：',vcode
    return vcode

# 浏览器截图
def screenshot(sel):
    # 截取当前网页，该网页有我们需要的验证码
    sel.save_screenshot(screenshot_path)
    # 通过xpath定位验证码
    imgelement = sel.find_element_by_id("captcha-img")
    # 获取验证码的x,y轴
    location = imgelement.location
    # 获取验证码的长宽
    size = imgelement.size
    rangle = (int(location['x']), \
              int(location['y']), \
              int(location['x']+size['width']), \
              int(location['y']+size['height']))
    # 打开截图
    i = Image.open(screenshot_path)
    # 使用Image的crop函数，从截图中再次截取我们需要的区域
    www_bcode = i.crop(rangle)
    # 保存截图查看效果
    www_bcode.save(screenshot_path_bcode)
    return www_bcode

# input by id 取值类型输入
def input_by_id(id_name,value,remark):
    try:
        print u'正在输入',remark
        user_input = sel.find_element_by_id(id_name)
        user_input.clear()
        user_input.send_keys(value)
        print u'输入成功'
    except:
        print '输入发生异常'

def open_browser():
    print u'打开浏览器'
    # 驱动的绝对路径，驱动下载地址：https://sites.google.com/a/chromium.org/chromedriver/home
    sel = webdriver.Chrome(hromedriver_exe_path)
    sel.implicitly_wait(30)
    return sel

# 使用自动化测试工具selenium + google浏览器驱动chromedriver 编写网页自动登录脚本
def login(sel):
    # 打开登录页面
    print u'打开登录页面'
    # 设置登录网址
    sel.get(login_url)

    # 输入用户名
    input_by_id("username",login_name,"用户名")
    # 输入密码
    input_by_id("password",login_pwd,"密码")

    # 验证码，图片识别
    www_bcode = screenshot(sel)
    # 准备识别验证码
    bcode = calc_bcode(www_bcode)
    # 输入验证码
    input_by_id("captcha",bcode,"验证码")

    # 点击提交按钮登录，如果网页提交按钮上没有id没有name，也没有其他合适的属性，可以通过xpath的方法获取：
    # 1，在网页中的提交按钮上右键，选择检查，此时会打开浏览器调试的Elements选项卡界面
    # 2，然后在提交按钮的代码上，再次右键，选择copy >> copy xpath即可

    print u'开始登陆'
    sel.find_element_by_id("submit").click()

    return sel

# 检测是否登录成功，如果没有就重新去执行登录操作
def login_ck(sel):
    # 检查是否登录成功
    print u'检查是否登录成功'
    curpage_url = sel.current_url
    print curpage_url.find('login')
    if curpage_url.find('login') == -1:
        print u'登录成功!'
    else:
        print u'登录失败，准备再次登录'
        # 重新调用
        to_login(sel)

# 登录成功后执行的内容
def success():
    print u'恭喜你，登录成功！！！20秒后自动关闭浏览器'
    time.sleep(20)
    # 关闭
    sel.quit()
    print u'浏览器已关闭！'

# 去执行登录操作
def to_login(sel):

    # 调用登录
    sel = login(sel)

    # 检查登录情况
    login_ck(sel)

    # 执行登录成功的方法
    success()

if __name__ == '__main__':

    # 打开浏览器
    sel = open_browser()

    # 去登陆
    to_login(sel)
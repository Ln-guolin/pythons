#!/usr/bin/env python
#coding=utf-8
#author=guolin

from selenium import webdriver
import time
import sys
reload(sys)
sys.setdefaultencoding( "utf-8")

# google浏览器驱动文件chromedriver.exe地址
hromedriver_exe_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

# 网站登录信息，本例以阿里云后台网站登录为例
login_url = 'http://signin.aliyun.com/2341234134/login.htm'
login_name = 'xxxx@21424312341234'
login_pwd = 'sxxxxxx'
#跳转到处理页面
calc_page ='https://ons.console.aliyun.com/'

# input by name 取值类型输入
def input_by_name(name,value,remark):
    try:
        print u'正在输入',remark
        user_input = sel.find_element_by_name(name)
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
    input_by_name("user_principal_name",login_name,"用户名")
    time.sleep(0.5)
    #点击确定按钮
    sel.find_element_by_xpath("//*[@id=\"J_FormNext\"]/span").click()
    time.sleep(0.5)
    # 输入密码
    input_by_name("password_ims",login_pwd,"密码")
    time.sleep(0.5)
    #点击确定按钮登录
    sel.find_element_by_xpath("//*[@id=\"u22\"]/input").click()

    print u'开始登陆'

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
    print u'恭喜你，登录成功！！！跳转到控制台'
    sel.get(calc_page)
    # 休眠10分钟
    time.sleep(600)
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
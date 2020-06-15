#!/usr/bin/env python
#coding=utf-8
#author=guolin
import requests  
import json  
import sys 
reload(sys)
sys.setdefaultencoding( "utf-8")
 
# pos请求
def req_post():  
    # 接口地址
    url = "http://openapi.xxx.com/v1/xxx.do"
    # 头部信息
    headers = {"Content-Type":"application/json"}     
    # 接口传送的参数
    data = {                                          
        "PARAMS": '{"test":1}',
        "CMD": 'TSA007'
    }  
    # 发送请求
    r = requests.post(url = url,json = data,headers = headers)
    
    # 响应信息
    print u'req_pos text=',r.text                                               
    print u'req_pos status_code=', r.status_code 
    return r
 
# get请求 
def req_get():  
 
    # 接口地址
    url = "http://openapi.xxx.com/v1/xxx.do"
    # 头部信息
    headers = {"Content-Type":"application/json"}
    # 参数
    params = {
        "tid":"aa",
        "memberId":123
    }
    # 发送请求
    r = requests.get(url = url,params = params,headers = headers)
    
    # 响应信息
    print u'req_get text=',r.text                                               
    print u'req_get status_code=', r.status_code 
    return r
 
    
if __name__=="__main__":  
    req_post()  
    req_get()
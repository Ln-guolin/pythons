#!/usr/bin/env python
#coding=utf-8
#author=guolin
from pymongo import MongoClient 
import sys 
reload(sys)
sys.setdefaultencoding( "utf-8")
import json
 
 
def get_param_mongo():
    
    print u'正在连接mongo...'
    try:
        conn = MongoClient("127.0.0.1", 27017)
        db = conn["mydb"]
        # 如果注释下面这行代码，表示非认证方式链接
        db.authenticate("user", "pwd")
        my_set = db["test1"]
        
        
        print u'执行[查询]操作...'
        
        dict = {"cmd":"TSA007","request.APP_SO_NUM_ID":"1234"}
        
        print u'命令：',dict
            
        data = my_set.find(dict)
       
        for result in data:
           return json.dumps(result["params"])
    
    except Exception as e:
        print(e)
 
 
    
if __name__=="__main__": 
 
    get_param_mongo()
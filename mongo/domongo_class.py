#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author=guolin
from pymongo import MongoClient
import sys 
reload(sys)
sys.setdefaultencoding( "utf-8")
import json
 
settings = {
    "host":'soilove.cn',#host
    "port":27017,#端口
    "db_name" : "cashbook",#数据库名字
    "collection" : "books",#集合名字
    "user" : "cashbookuser",#用户名
    "pwd" : "123456"#密码
}
 
class TestMongoDB(object):
    def __init__(self):
        print("正在连接mongo...")
        try:
            self.conn = MongoClient(settings["host"], settings["port"])
        except Exception as e:
            print(e)
        self.db = self.conn[settings["db_name"]]
        # 如果注释下面这行代码，表示非认证方式链接
        self.db.authenticate(settings["user"], settings["pwd"])
        self.my_set = self.db[settings["collection"]]
 
    def insert(self,dic):
        print("执行[插入]操作...")
        self.my_set.insert(dic)
 
    def save(self,dic):
        print("执行[保存]操作...")
        self.my_set.save(dic)
 
    def update(self,dic,newdic):
        print("执行[修改]操作...")
        self.my_set.update(dic,newdic)
 
    def delete(self,dic):
        print("执行[删除]操作...")
        self.my_set.remove(dic)
 
    def find(self,dic):
        print("执行[查询]操作...")
        data = self.my_set.find(dic)
        for result in data:
            print(result)
 
def main():
    mongo = TestMongoDB()
    mongo.insert({"bookid":1,"bookname":"语文"})
    mongo.find({"bookid":1})
 
    mongo.update({"bookid":1},{"$set":{"bookname":"数学"}})
    mongo.find({"bookid":1})
 
    mongo.save({"bookid":1,"bookname":"语文"})
    mongo.save({"bookid":2,"bookname":"英语"})
    mongo.find({"bookid":1})
    mongo.find({"bookid":2})
 
    mongo.delete({"bookid":1})
    mongo.find({"bookid":1})
 
if __name__ == "__main__":
    main()
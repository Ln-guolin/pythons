#!/usr/bin/env python
#coding=utf-8
#author=guolin
import MySQLdb
import sys 
reload(sys)
sys.setdefaultencoding( "utf-8")
 
def test_db():
    try:
    
        conn = MySQLdb.connect(host='172.28.1.6',user='root',passwd='123456',db='testdb',port=3306,charset="utf8")
        cur = conn.cursor()
        
        nm = cur.execute('select * from t_tag limit 2')
        list = cur.fetchmany(nm)
        
        for item in list:
            print item[0]
        #conn.commit()    
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
 
if __name__=="__main__": 
 
    test_db(url)
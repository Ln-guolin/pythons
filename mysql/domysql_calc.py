#!/usr/bin/env python
#coding=utf-8
#author=guolin
import pymysql
import sys 
reload(sys)
sys.setdefaultencoding( "utf-8")

# 创建连接
conn = pymysql.connect(
    host='rm-bp738r7jo.mysql.rds.aliyuncs.com',
    port=3306,
    user='testadmin',
    password='22222',
    db='sc',
    charset='utf8')


def insert():
    # sql语句
    sql = "insert into `sg_uc`.`operation_logs` ( `user_code`, `module`, `method`, `api_path`, `param`, `create_time`, `update_time`) values ('testpy', 'ttttt  py', 'test py', '/admin/testpy','测试一下',now(), now());"
    print u'[insert]SQL='+sql
    # 执行
    result = cursor.execute(sql)
    # 提交事务
    conn.commit()
    print u'[insert]结果=',result

def delete():
    # sql语句
    sql = "delete from operation_logs where user_code = 'testpy';"
    print u'[delete]SQL='+sql
    # 执行
    result = cursor.execute(sql)
    # 提交事务
    conn.commit()
    print u'[delete]结果=',result

def update():
    # sql语句
    sql = "update operation_logs set module = 'has update' where user_code = 'testpy';"
    print u'[update]SQL='+sql
    # 执行
    result = cursor.execute(sql)
    # 提交事务
    conn.commit()
    print u'[update]结果=',result

def query():
    # sql语句
    sql = "select * from operation_logs where user_code = 'testpy';"
    print u'[query]SQL='+sql

    # 执行
    result = cursor.execute(sql)
    print u'[query]结果=',result

    # 查询单条结果
    #data = cursor.fetchone()
    #print u'查询结果=',data

    # 查询多条结果
    datas = cursor.fetchall()
    for row in datas:
        print u'批量查询结果=',row

if __name__=="__main__":

    # 创建游标
    cursor = conn.cursor()
    try:
        insert()

        query()

        update()

        delete()
    except Exception as e:
        print u'执行异常：',e
    finally:
        # 关闭游标和连接
        cursor.close()
        conn.close()
        print u'关闭数据库连接！'
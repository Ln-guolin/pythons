#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author=guolin
import redis

# 普通连接
def conn():
    # 如需非认证方式，去掉password即可
    r = redis.Redis(host='soilove.cn', port=6379,db=0,password='123456')
    return r
    
# 连接池
def conn_pool():
    # 如需非认证方式，去掉password即可
    pool = redis.ConnectionPool(host='soilove.cn', port=6379,db=0,password='123456')
    r = redis.Redis(connection_pool=pool)
    return r

# redis 最基本操作
def calc_basic(r):
    # 简单的set，get
    r.set('name', 'zhangsan')
    print u'简单的set，get:',r.get('name')
    
    # setex设置过期时间（秒）
    r.setex('name', 'zhangsan', 10)
    
    # getrange根据字节获取值
    print u'getrange根据字节获取值:',r.getrange("name",0,3)
    
    # strlen获取值长度
    print u'strlen获取值长度:',r.strlen("name")
    
    # incr自增和decr自减
    r.incr('num_a', 2)
    print u'incr自增:',r.get('num_a')
    r.decr('num_a', 1)
    print u'incr自减:',r.get('num_a')
    
# redis hash操作
def calc_hash(r):
    print u'############ redis hash操作 ############'
    
    # hset,hget普通设值和获取值
    r.hset("hset_users","zhangsan","18")
    r.hset("hset_users","lisi","21")
    
    print u'hset,hget普通设值和获取值:',r.hget("hset_users","zhangsan")
    print u'hset,hget普通设值和获取值:',r.hget("hset_users","lisi")
   
    # hdel删除键值对
    r.hdel("hset_users","zhangsan")
    
    # hgetall获取全部
    print u'hgetall获取全部:',r.hgetall("hset_users")
    
    # hmset批量设值和批量获取值
    users = {"zhangsan":"19","lisi":"22"}
    r.hmset("hset_users",users)
    
    userkey = ["zhangsan","lisi"]
    print u'hmget批量获取值:',r.hmget("hset_users",userkey)
    print u'hmget批量获取值...args:',r.hmget("hset_users","zhangsan","lisi")
    
    # hexists判断是否存在
    exists = r.hexists("hset_users","zhangsan")
    print u'hexists判断是否存在:',exists
    
    # hlen获取键值对个数
    print u'hlen获取键值对个数:',r.hlen("hset_users")

    # hkeys获取所有的key
    print u'hkeys获取所有的key:',r.hkeys("hset_users")

    # hvals获取所有的value
    print u'hvals获取所有的value:',r.hvals("hset_users")

# redis list操作
def calc_list(r):
    print u'############ redis list操作 ############'
    # lpush从左添加元素
    r.lpush("list_name",2)
    r.lpush("list_name",3,4,5)#保存在列表中的顺序为5，4，3，2
    
    # rpush从右添加元素
    r.lpush("list_name",6)
    
    # llen获取元素个数
    print u'llen获取元素个数:',r.llen('list_name')
    
    # lindex获取元素
    print u'lindex获取元素:',r.lindex("list_name",0)
    
    # lrange分片获取元素
    print u'lrange分片获取元素:',r.lrange("list_name",0,-1)
    
    # lpop从左删除和rpop从右删除元素
    print u'lpop从左删除:',r.lpop("list_name")
    print u'rpop从右删除元素:',r.rpop("list_name")
    
    # delete删除集合
    r.delete('list_name')


# redis set操作
def calc_set(r):
    print u'############ redis set操作 ############'
    # sadd添加元素
    r.sadd("set_name","yuwen")
    r.sadd("set_name","yuwen","shuxue")
    
    # smembers获取元素
    print u'smembers获取元素:',r.smembers("set_name")
    
    # scard获取集合元素个数
    print u'scard获取集合元素个数:',r.scard("set_name")
    
    # srandmember随机获取n个元素
    print u'srandmember随机获取n个元素:',r.srandmember("set_name",2) 
    
    # sismember查询集合当中是否包含元素
    print u'sismember查询集合当中是否包含元素:',r.sismember("set_name","yuwen") 
    
    # srem移除元素
    r.srem('set_name','yuwen')
    print u'srem移除元素后:',r.smembers("set_name")
    
    # delete删除集合
    r.delete('set_name')
    

if __name__ == "__main__":

    # 获取连接，可以通过下面2个方式
    #r = conn()
    r = conn_pool()
    
    # 调用示例
    calc_basic(r)
    calc_hash(r)
    calc_set(r)
    calc_list(r)
    
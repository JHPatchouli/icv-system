#使用SQLAlchemy写一个连接mysql数据库并且映射表到对象的例程
import os

from flask import Flask
from flask_redis import FlaskRedis
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#redis配置
redis_client=None



# 创建数据库连接
engine = create_engine('mysql+pymysql://icv-system:mysql_cpgNlegR@172.23.99.9/icv-system')

Session = sessionmaker(bind=engine)

# 创建对象的基类:
Base = declarative_base()
distributed_lock=None
flag=0
flag_lk=True
pid = os.getpid()
print("PID:"+str(pid))
#redis处理类
class RedisClient:
    global flag_lk, pid, redis_client, distributed_lock, flag
    def __init__(self, app:Flask, host:str, port:int, password:str, db:str):
        global flag_lk, pid, redis_client, distributed_lock, flag
        self.app=app
        self.host=host
        self.port=int(port)
        self.password=password
        self.db=db
        # flask-redis 的配置和初始化
        app.config['REDIS_URL'] = 'redis://:{}@{}:{}/{}'.format(self.password, self.host, self.port, self.db)
        self.redis_client = FlaskRedis(app)
        self.distributed_lock=self.redis_client.lock('redis_lock',timeout=10)
    
    def get_all_data(self):
        # 获取所有数据
        keys = self.redis_client.keys('*')  # 获取所有 key
        all_data = {}
        for key in keys:
            value = self.redis_client.get(key)
            all_data[key.decode()] = value.decode()
        return all_data
    
    def expire(self,key:str,timeout:str):
        return self.redis_client.expire(key,timeout)
    
    def lock(self):
        return self.distributed_lock
    
    def flushdb(self):
        # 删除所有数据
        self.redis_client.flushdb()
    
    def set(self, key, value):
        # 设置数据
        self.redis_client.set(key, value)
        
    def delete(self, key):
        # 删除数据
        self.redis_client.delete(key)
        
    def get(self, key):
        # 获取数据
        return self.redis_client.get(key)
    
RD_ORM:RedisClient=None
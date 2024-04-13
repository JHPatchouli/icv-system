#使用SQLAlchemy写一个连接mysql数据库并且映射表到对象的例程
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 创建数据库连接
engine = create_engine('mysql+pymysql://root:mysql_Sahx3a5b6j1@172.23.99.9/icv-system')

Session = sessionmaker(bind=engine)

# 创建对象的基类:
Base = declarative_base()
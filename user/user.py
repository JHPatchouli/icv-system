import hashlib
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from orm.icv_orm import Base, engine, Session
# 定义User对象:
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True,nullable=False,autoincrement=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    admin=Column(Integer(), nullable=False)
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# 创建数据表
Base.metadata.create_all(engine)
# 创建User对象的操作
def create_user(username,password,admin):
    session = Session()
    new_user = User(username=username, password=md5_with_salt(password),admin=admin)
    session.add(new_user)
    session.commit()
    session.close()
    
def get_user(username):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    session.close()
    return user

def get_all_user():
    session = Session()
    users = session.query(User).all()
    session.close()
    return users

def update_user(id, username, password,admin):
    session = Session()
    user = session.query(User).filter_by(id=id).first()
    user.username = username
    user.password = md5_with_salt(password)
    user.admin=admin
    session.commit()

        
def delete_user(id):
    session = Session()
    user = session.query(User).filter_by(id=id).first()
    session.delete(user)
    session.commit()
    session.close()

#密文生成
salt = "vP7fZcWSPbTLbWwOwhRf8gGdq9IdPkbr"
def md5_with_salt(password):
    global salt
    # 将盐拼接到密码前面
    salted_password = salt + password
    # 计算MD5哈希值
    hashed_password = hashlib.md5(salted_password.encode()).hexdigest()
    return hashed_password
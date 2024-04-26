import time

from flask import (Blueprint, Flask, jsonify, redirect, request, session,
                   url_for)
#允许跨域访问
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

import cars.cars as cars_fun
import orm.icv_orm as redis_orm
from cards.router import cards_br
from cars.router import cars_br
from flask_session import Session
from redis_test.router import redis_br
from user.router import user_br

app=Flask(__name__)

#实例化Redis类
redis_orm.RD_ORM=redis_orm.RedisClient(app=app,host='172.23.99.9',port=6379,password='jhkdjhkjdhsIUTYURTU_sDjsQs',db='0')
# print(type(redis_orm.RD_ORM))
#进入竞选
cars_fun.get_redis_thread()
#session配置
app.config['SECRET_KEY'] = '19943272031cece2ac924f34c2ebfc33'
app.config['SESSION_TYPE'] = 'filesystem'  # 可以选择其他类型的会话存储，如 'redis' 等
Session(app)

#蓝图配置
app.register_blueprint(cars_br)
app.register_blueprint(cards_br)
app.register_blueprint(user_br)
app.register_blueprint(redis_br)

#跨域配置
CORS(app)

#根路由
@app.route('/')
def cars_index():
    return 'Error'

#主进程
if __name__ == '__main__':
    #实例化Redis类redis_orm
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run()
    
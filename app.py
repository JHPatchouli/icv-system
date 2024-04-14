#写一个flask蓝本，路由存在cars模块中
from flask import Flask, request, jsonify, Blueprint, session, redirect, url_for
from flask_session import Session
from cars.router import cars_br
from cards.router import cards_br
from user.router import user_br 
#允许跨域访问
from flask_cors import CORS

app=Flask(__name__)

app.config['SECRET_KEY'] = '19943272031cece2ac924f34c2ebfc33'
app.config['SESSION_TYPE'] = 'filesystem'  # 可以选择其他类型的会话存储，如 'redis' 等
# app.config['PERMANENT_SESSION_LIFETIME'] = 20  # 设置会话过期时间，单位为秒
Session(app)

app.register_blueprint(cars_br)
app.register_blueprint(cards_br)
app.register_blueprint(user_br)
CORS(app)
@app.route('/')
def cars_index():
    return 'Error'

if __name__ == '__main__':
    #main
    app.run(debug=False,host='127.0.0.1',port=5000)
    
    #dev
    #app.run(debug=True,host='127.0.0.1',port=5001)
    
    #new
    #app.run(debug=True,host='127.0.0.1',port=5001)

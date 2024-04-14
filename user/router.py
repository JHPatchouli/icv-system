import json
from flask import Flask, request, jsonify, Blueprint, session, redirect, url_for
from flask_session import Session
import user.user as Obj_User
user_br=Blueprint('login',__name__,template_folder='templates')

@user_br.route('/api/user/login',methods=['POST'])
def login():
    # 获取前端传递的参数
    username = request.form.get('username')
    password = request.form.get('password')
    try:
        user_info=Obj_User.get_user(username=username)
        if(user_info.password==Obj_User.md5_with_salt(password)):
            session['username'] = username
            session['admin'] = user_info.admin # 设置管理员标志位
            session.permanent = True  # 设置会话为永久性会话
            return json.dumps({'status': '200', 'message': 'success','data':''},sort_keys=False)
        else:
            return json.dumps({'status': '400', 'message': 'fail','data':''},sort_keys=False)
    except:
        return json.dumps({'status': '400', 'message': 'fail','data':''},sort_keys=False)

    

#退出登录
@user_br.route('/api/user/logout',methods=['GET'])
def logout():
    # 清除session
    session.pop('username', None)
    session.pop('admin', None)
    
    return json.dumps({'status': '200', 'message': 'success','data':''},sort_keys=False)


#用于测试判断session是否有效
@user_br.route('/api/user/check',methods=['GET'])
def check():
    if 'username' in session:
        if session.get('admin')==1:
            return json.dumps({'status': '200', 'message': 'success','data':"admin"},sort_keys=False)
        else:
            return json.dumps({'status': '200', 'message': 'success','data':str(session.get('admin'))},sort_keys=False)
    else:
        return json.dumps({'status': '400', 'message': 'fail','data':''},sort_keys=False)
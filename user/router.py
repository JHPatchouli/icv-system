from flask import Flask, request, jsonify,Blueprint
#使用session控制保持会话
# from flask_session import Session
import user.login as Obj_User
user_br=Blueprint('login',__name__,template_folder='templates')
# Session = Session()
@user_br.route('/api/user/login',methods=['POST'])
def login():
    # 获取前端传递的参数
    username = request.form.get('username')
    password = request.form.get('password')
    if(Obj_User.get_user(username=username).password==Obj_User.md5_with_salt(password)):
        return jsonify({'status': '200', 'message': 'success','data':''})
    else:
        return jsonify({'status': '400', 'message': 'fail','data':''})

    
    
    
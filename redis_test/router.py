import json
from flask import Flask, request, jsonify, Blueprint, session, redirect, url_for
from flask_session import Session
import orm.icv_orm as redis_orm

redis_br=Blueprint('redis',__name__,template_folder='templates')

@redis_br.route('/redis',methods=['GET'])
def redis_all():
    global redis_orm
    return redis_orm.RD_ORM.get_all_data()

#添加数据
@redis_br.route('/redis/add',methods=['POST'])
def redis_add():
    global redis_orm
    if request.method == 'POST':
        key = request.form.get('key')
        data = request.form.get('data')
        redis_orm.RD_ORM.set_data(key,data)
        return "ok"
    return "ok"

#查询数据
@redis_br.route('/redis/query/<key>',methods=['GET'])
def redis_query(key):
    global redis_orm
    return redis_orm.RD_ORM.get_data(key)

#删除所有redis数据
@redis_br.route('/redis/delete',methods=['GET'])
def redis_delete():
    global redis_orm
    redis_orm.RD_ORM.del_all_data()
    return json.dumps(redis_orm.RD_ORM.get_all_data(),sort_keys=False)
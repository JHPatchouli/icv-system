#写一个被Flask调用的路由模块
import json

from flask import Blueprint, Flask, request, session

import cars.cars as cars
import orm.icv_orm as redis_orm
from cars.cars_router import router_All
from flask_session import Session

cars_br=Blueprint('cars',__name__,template_folder='templates')

@cars_br.route('/api/cars/car_info/<int:id>', methods=['GET'])
def get_cars_info(id:int):
    if(redis_orm.RD_ORM.get("session_cookie_id")==None):
        session['update']=True
        session_cookie_id = session.sid
        redis_orm.RD_ORM.set("session_cookie_id",session_cookie_id)
        redis_orm.RD_ORM.expire('session_cookie_id', 2)
    elif(redis_orm.RD_ORM.get("session_cookie_id").decode() in "None"):
        session['update']=True
        session_cookie_id = session.sid
        redis_orm.RD_ORM.set("session_cookie_id",session_cookie_id)
        redis_orm.RD_ORM.expire('session_cookie_id', 2)
    if(redis_orm.RD_ORM.get("session_cookie_id").decode() in session.sid):
        session['update']=True
        session_cookie_id = session.sid
        redis_orm.RD_ORM.set("session_cookie_id",session_cookie_id)
        redis_orm.RD_ORM.expire('session_cookie_id', 2)
    cars_data=json.loads(redis_orm.RD_ORM.get("cars_data").decode())
    # print(cars_data[id-1])
    return_data={
        "status": 200,
        "msg": "success",
        "data": {
            "car_status": cars_data[id-1]['data']['status'],
            "car_speed": cars_data[id-1]['data']['speed'],
            "car_loc": router_All[id-1][cars_data[id-1]['data']['index']],
            "car_power": cars_data[id-1]['data']['power'],
            "car_pos": "-1",
        }
    }
    if('update' in session and redis_orm.RD_ORM.get("session_cookie_id").decode() == session.sid):
        if(session.get('update')):
            cars.update_index(id)
    print(session.sid)
    print("redis:"+redis_orm.RD_ORM.get("session_cookie_id").decode())
    return json.dumps(return_data,sort_keys=False)

@cars_br.route('/api/cars/setspeed/<int:id>/<int:speed>', methods=['GET'])
def set_cars_speed(id:int,speed:int):
    cars.fake_cars_speed[id-1]['speed']=speed
    #打包字典数据返回json
    car_speed = {'status': 200, 'msg': 'success', 'data': speed}
    return json.dumps(car_speed,sort_keys=False)    

@cars_br.route('/api/cars/setstatus/<int:id>/<int:status>', methods=['GET'])
def set_cars_status(id:int,status:int):
    cars.fake_cars_status[id-1]['status']=status
    #打包字典数据返回json
    car_status = {'status': 200, 'msg': 'success', 'data': status}
    return json.dumps(car_status,sort_keys=False)
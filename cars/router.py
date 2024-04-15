#写一个被Flask调用的路由模块
from flask import Flask, request,Blueprint
import json
import cars.cars as cars
cars_br=Blueprint('cars',__name__,template_folder='templates')
pub_speed={}
# @cars_br.route('/api/cars/speed/<int:id>', methods=['GET'])
# def get_cars_speed(id:int):
#     global pub_speed
#     try:
#         ret_speed=pub_speed[id]
#         #打包字典数据返回json
#         car_speed = {'status': 200, 'msg': 'success', 'data': ret_speed}
#         return json.dumps(car_speed,sort_keys=False)
#     except:
#         #打包字典数据返回json
#         car_speed = {'status': 200, 'msg': 'success', 'data': 0}
#         return json.dumps(car_speed,sort_keys=False)
@cars_br.route('/api/cars/car_info/<int:id>', methods=['GET'])
def get_cars_info(id:int):
    #打包字典数据返回json
    car_info = {'status': 200, 'msg': 'success', 'data': cars.fake_data[id-1]}
    return json.dumps(car_info,sort_keys=False)

@cars_br.route('/api/cars/setspeed/<int:id>/<int:speed>', methods=['GET'])
def set_cars_speed(id:int,speed:int):
    global pub_speed
    pub_speed[id]=speed
    #打包字典数据返回json
    car_speed = {'status': 200, 'msg': 'success', 'data': speed}
    return json.dumps(car_speed,sort_keys=False)    
#写一个被Flask调用的路由模块
import json

from flask import Blueprint, Flask, request

import cars.cars as cars

cars_br=Blueprint('cars',__name__,template_folder='templates')

@cars_br.route('/api/cars/car_info/<int:id>', methods=['GET'])
def get_cars_info(id:int):
    #打包字典数据返回json
    speed=cars.fake_cars_speed[id-1]['speed']
    # print(speed)
    loc=cars.fake_data[id-1]['data']
    # print(loc)
    power=cars.fake_cars_power[id-1]['power']
    # print(power)
    fake_data_rt={'car_status':1,'car_speed':speed,'car_loc':loc}
    car_info = {'status': 200, 'msg': 'success', 'data': fake_data_rt}
    if(cars.fake_car_loc(id)==False):
        # print("FFFFF")
        return json.dumps({'status': 200, 'msg': 'success', 'data': "err"},sort_keys=False)
    return json.dumps(car_info,sort_keys=False)

@cars_br.route('/api/cars/setspeed/<int:id>/<int:speed>', methods=['GET'])
def set_cars_speed(id:int,speed:int):
    cars.fake_cars_speed[id-1]['speed']=speed
    #打包字典数据返回json
    car_speed = {'status': 200, 'msg': 'success', 'data': speed}
    return json.dumps(car_speed,sort_keys=False)
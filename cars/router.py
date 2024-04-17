#写一个被Flask调用的路由模块
from flask import Flask, request,Blueprint
import json
import cars.cars as cars
cars_br=Blueprint('cars',__name__,template_folder='templates')

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
    speed=cars.fake_cars_speed[id-1]['speed']
    # print(speed)
    loc=cars.fake_data[id-1]['data']
    # print(loc)
    power=cars.fake_cars_power[id-1]['power']
    # print(power)
    fake_data_rt={'car_status':1,'car_speed':speed,'car_loc':loc,'car_power': power,'car_pos': '-1'}
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

@cars_br.route('/api/cars/setstatus/<int:id>/<int:status>', methods=['GET'])
def set_cars_status(id:int,status:int):
    cars.fake_cars_status[id-1]['status']=status
    #打包字典数据返回json
    car_status = {'status': 200, 'msg': 'success', 'data': status}
    return json.dumps(car_status,sort_keys=False)
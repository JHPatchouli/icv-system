#写一个被Flask调用的路由模块
from flask import Flask, request, jsonify,Blueprint

cars_br=Blueprint('cars',__name__,template_folder='templates')
pub_speed={}
for i in range(1,101):
    pub_speed[i]=0


@cars_br.route('/api/cars/speed/<int:id>', methods=['GET'])
def get_cars_speed(id):
    global pub_speed
    try:
        ret_speed=pub_speed[id]
        #打包字典数据返回json
        car_speed = {'status': 200, 'msg': 'success', 'data': ret_speed}
        return jsonify(car_speed)
    except:
        #打包字典数据返回json
        car_speed = {'status': 204, 'msg': 'not found', 'data': None}
        return jsonify(car_speed)



@cars_br.route('/api/cars/setspeed/<int:id>/<int:speed>', methods=['GET'])
def set_cars_speed(id,speed):
    global pub_speed
    pub_speed[id]=speed
    #打包字典数据返回json
    car_speed = {'status': 200, 'msg': 'success', 'data': speed}
    return jsonify(car_speed)
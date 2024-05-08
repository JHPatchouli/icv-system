import json
import random
import time

import cards.cards as Obj_Card
import cars.cars as cars

start_time=[]
for i in range(0,4):
    add_time=random.randint(0,300)
    start_time.append(time.time()-add_time)

def car_cam_stream():
    data=[]
    num=cars.get_car_num()
    for i in range(0,num):
        data.append({
        'car_id': i+1,
        'cam_stream': "https://rtsp.mrhao.xyz/live/car_{}".format(i+1)
        # 'Identify': 
        #     {
        #         'traffic_light': random.choice(['red','yellow','green']),
        #         'other': 'other_data'
        #     }
        })
    return data

def cars_run_status():
    #使用字典
    # car_id:车辆编号（传入）
    # car_drive:是否正常行驶（默认真）
    # car_time:运行时长（当前进程运行时间，转换为中国时区标准UTC时间）

    data=[]
    num=cars.get_car_num()
    for i in range(0,num):
        end_time = time.time()
        runtime = end_time - start_time[i] - (8 * 3600)
        data.append({
            'car_id': i+1,
            'car_name': '智能网联车PIoT-VPro',
            'sensor': {'vision_sensor': 'Oline', 'ultrasonic_sensor': 'Oline', 'RFID_sensor': 'Oline','Gyroscope_sensor': 'Oline','WIFI_module': 'Oline'},
            'car_drive': True,
            'car_time': time.strftime("%H:%M:%S", time.localtime(runtime))
            })
    return data



def car_loc_info():
    data=[]
    num=cars.get_car_num()
    for i in range(0,num):
        loc=cars.fake_data[i]['data']
        card_info=Obj_Card.get_card(loc)
        data.append({
            'car_id': i+1,
            'r_num': card_info.r_num,
            'r_ide': card_info.r_ide,
            'r_type': card_info.r_type,
            'card_id': loc
        })
    return data

def car_power_status():
    data=[]
    num=cars.get_car_num()
    for i in range(0,num):
        data.append({
            "car_id": i+1,
            "car_power": random.randint(60,89),
            "car_power_status": random.choice([True,False])
        })
    return data

def car_gy_status():
    data=[]
    num=cars.get_car_num()
    for i in range(0,num):
        data.append({
            "car_id": i+1,
            "car_angle": {'yaw': random.randint(0,360),'pitch': random.randint(0,360),'roll': random.randint(0,360)},
            "car_acc": {'x': random.randint(0,1500),'y': random.randint(0,1500),'z': random.randint(0,1500)}
        })
    return data

def car_ult_data():
    data=[]
    num=cars.get_car_num()
    for i in range(0,num):
        data.append({
            "car_id": i+1,
            "forward_dis": random.randint(10,100),
            "backward_dis": random.randint(10,100),
            "left_dis": random.randint(10,100),
            "right_dis": random.randint(10,100)
        })
    return data



def car_cam_stream_single(id:int):
    data={
    'car_id': int(id),
    'cam_stream': "https://rtsp.mrhao.xyz/live/car_{}".format(id),
    'Identify': 
        {
            'traffic_light': random.choice(['red','yellow','green']),
            'other': 'other_data'
        }
    }
    return data

def car_loc_info_single(id:int):
    num=cars.get_car_num()
    loc=cars.fake_data[id-1]['data']
    card_info=Obj_Card.get_card(loc)
    data={
        'car_id': int(id),
        'card_id': loc,
        'inter_range': card_info.inter_range,
        'over_range': card_info.over_range,
        'park_range': card_info.park_range,
        'char_range': card_info.char_range
    }
    return data

def car_power_status_single(id:int):
    loc=cars.fake_data[id-1]['data']
    card_info=Obj_Card.get_card(loc)
    if(card_info.char_range=="1"):
        c_range=True
    else:
        c_range=False
    data={
        "car_id": int(id),
        "car_power": random.randint(60,89),
        "car_power_status": random.choice([True,False]),
        "c_range": c_range
    }
    return data

def car_gy_status_single(id:int):
    data={
        "car_id": int(id),
        "car_angle": {'yaw': random.randint(0,360),'pitch': random.randint(0,360),'roll': random.randint(0,360)},
        "car_acc": {'x': random.randint(0,1500),'y': random.randint(0,1500),'z': random.randint(0,1500)}
    }
    return data
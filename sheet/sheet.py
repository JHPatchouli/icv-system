import random
import time
import cards.cards as Obj_Card
import cars.cars as cars
start_time=[]
for i in range(0,4):
    add_time=random.randint(0,300)
    start_time.append(time.time()-add_time)

def cars_run_status(id:int):
    #使用字典
    # car_id:车辆编号（传入）
    # car_drive:是否正常行驶（默认真）
    # car_time:运行时长（当前进程运行时间，转换为中国时区标准UTC时间）
    end_time = time.time()
    runtime = end_time - start_time[id-1] - (8 * 3600) 
    data={
        'car_id': id,
        'car_drive': True,
        'car_time': time.strftime("%H:%M:%S", time.localtime(runtime))
        }
    return data

def car_cam_stream(id:int):
    data={
    'car_id': id,
    'cam_stream': "rtsp://rtsp.mrhao.xyz:8554/live/car_{}".format(id),
    'traffic_light': random.choice(['red','yellow','green'])
    }
    return data

def car_loc_info(id:int):
    speed=cars.fake_cars_speed[id-1]['speed']
    loc=cars.fake_data[id-1]['data']
    power=cars.fake_cars_power[id-1]['power']
    card_info=Obj_Card.get_card(loc)
    data={
        'car_id': id,
        'car_loc': card_info.r_num,
        'card_id': loc
    }
    return data

def car_ult_data(id:int):
    data={
        "car_id": id,
        "forward_dis": random.randint(10,100),
        "backward_dis": random.randint(10,100),
        "left_dis": random.randint(10,100),
        "right_dis": random.randint(10,100)
    }
    return data

def car_err_status(id:int):
    data={
        "car_id": id,
        "car_err": random.randint(0,20),
        "car_posture": True
    }
    return data

def car_power_status(id:int):
    data={
        "car_id": id,
        "car_power": random.randint(60,70),
        "car_power_status": random.choice([True,False])
    }
    return data
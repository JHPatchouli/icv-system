import random
import threading
import time

import cars.cars_router as cars_router

fake_cars_speed=[]
fake_cars_power=[]
fake_cars_status=[]
router_index=[]
fake_data=[]

def fake_data_init():
    for data in cars_router.router_All:
        # print(data)
        fake_data.append({"data":data[0]})
        fake_cars_speed.append({"speed": 3})
        fake_cars_power.append({"power": random.randint(20, 100)})
        fake_cars_status.append({'status': 1})
        router_index.append(0)
        

def get_car_num():
    return len(cars_router.router_All)

def fake_car_loc(id:int):
    global router_index
    global fake_data
    #改为500毫秒更改一次信息
    # cycle_time = 500
    # while True:
    #     current_time = int(round(time.time() * 1000))
    #     current_second = current_time % cycle_time
    #     if current_second == 0:
    if(id>len(cars_router.router_All)):
        return False
    router_index[id-1]=(router_index[id-1]+1)%len(cars_router.router_All[id-1])
    # print("index:"+str(router_index[id-1]))
    fake_data[id-1]={"data":int(cars_router.router_All[id-1][router_index[id-1]])}
    # print("fake_data:"+str(fake_data[id-1]))
        # time.sleep(0.001)
# print(cars_router.router_3)
fake_data_init()
# 创建一个线程来执行红绿灯逻辑
# fake_data_thread = threading.Thread(target=fake_car_loc)
# fake_data_thread.daemon = True  # 设置为守护线程，主线程结束时自动退出
# fake_data_thread.start()
# print("开启线程")
import json
import os
import random
import threading
import time

import cars.cars_router as cars_router
import orm.icv_orm as redis_orm

#基准速度
sim_speed=5
#基准延时
sim_time=390


#速度列表
fake_cars_speed=[]
#电量列表
fake_cars_power=[]
#状态列表
fake_cars_status=[]
#路径下标
router_index=[]
# 临时数据
fake_data=[]
#进程ID
pid = os.getpid()

#写入资格标志位
WIN=False

#数据初始化
def fake_data_init():
    global fake_cars_speed, fake_cars_power, fake_cars_status, router_index, fake_data
    for id in list(range(0,len(cars_router.router_All))):
        fake_cars_speed.append({"speed": random.randint(3, 5)})
        fake_cars_power.append({"power": random.randint(20, 100)})
        fake_cars_status.append({'status': 1})
        router_index.append(0)
    for speed,power,status,index in zip(fake_cars_speed,fake_cars_power,fake_cars_status,router_index):
        fake_data.append(
            {"data": 
                {
                    'speed': speed['speed'],
                    'power': power['power'],
                    'status': status['status'],
                    'index': index
                }
            })

#进行初始化
fake_data_init()   
#竞选写入资格
def get_redis_thread():
    global pid, redis_orm, distributed_lock, WIN, fake_data
    time.sleep(0.01)
    distributed_lock = redis_orm.RD_ORM.lock()  # 获取分布式锁
    if distributed_lock.acquire(blocking=False):
        try:
            
            print("PID:" + str(pid) + '--WT')
            time.sleep(5)
        finally:
            redis_orm.RD_ORM.flushdb()
            # distributed_lock.release()  # 释放分布式锁
            print("PID:" + str(pid) + '--Lock released')
            print("PID" + str(pid) + '--WINWINWINWINWINWIN')
            time.sleep(2)
            redis_orm.RD_ORM.set("cars_data",json.dumps(fake_data,sort_keys=False))
            redis_orm.RD_ORM.set("session_cookie_id","None")
            redis_orm.RD_ORM.set("session_flag","0")
            # WIN=True
            # if WIN:
            #     print("Start Thread")
            #     write_thread = threading.Thread(target=update_index)
            #     write_thread.start()
            # return
    else:
        print("PID:" + str(pid) + '--KILL')
        return



#路径更新线程
def update_index(id:int):
    cars_data=json.loads(redis_orm.RD_ORM.get("cars_data").decode())
    id-=1
    cars_data[id]['data']['index']=(cars_data[id]['data']['index']+1)%len(cars_router.router_All[id])
    redis_orm.RD_ORM.set("cars_data",json.dumps(cars_data,sort_keys=False))

#获得写入资格
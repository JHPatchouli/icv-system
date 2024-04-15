import threading
import time
import cars.cars_router as cars_router
fake_cars_dict={}
router1_index=0
router2_index=0
router3_index=0
router4_index=0
fake_data=[]
# flag=0
# current_time=0
# current_second=0
def fake_car_info():
    global router1_index,router2_index,router3_index,router4_index
    global fake_data
    #改为500毫秒更改一次信息
    cycle_time = 500
    while True:
        current_time = int(round(time.time() * 1000))
        current_second = current_time % cycle_time
        if current_second == 0:
            router1_index=(router1_index+1)%len(cars_router.router_1)
            router2_index=(router2_index+1)%len(cars_router.router_2)
            router3_index=(router3_index+1)%len(cars_router.router_3)
            router4_index=(router4_index+1)%len(cars_router.router_4)
            fake_data=[{"data":int(cars_router.router_All[1-1][router1_index])}]
            fake_data+=[{"data":int(cars_router.router_All[2-1][router2_index])}]
            fake_data+=[{"data":int(cars_router.router_All[3-1][router3_index])}]
            fake_data+=[{"data":int(cars_router.router_All[4-1][router4_index])}]
        time.sleep(0.001)



# 创建一个线程来执行红绿灯逻辑
fake_data_thread = threading.Thread(target=fake_car_info)
fake_data_thread.daemon = True  # 设置为守护线程，主线程结束时自动退出
fake_data_thread.start()
print("开启线程")
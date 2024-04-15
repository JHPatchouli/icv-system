# from flask import Flask, jsonify
# import threading
# import time

# app = Flask(__name__)
# traffic_light_color = 'Green'  # 初始值为绿灯

# def traffic_light_logic():
#     global traffic_light_color
#     cycle_time = 60  # 红绿灯一个周期的时间（秒）
#     while True:
#         current_time = int(time.time())  # 获取当前时间戳
#         current_second = current_time % cycle_time

#         # 根据当前秒数判断红绿灯状态
#         if current_second < 30:
#             traffic_light_color = 'Green'
#         else:
#             traffic_light_color = 'Red'

#         time.sleep(1)  # 每秒检查一次

# # 创建一个线程来执行红绿灯逻辑
# light_thread = threading.Thread(target=traffic_light_logic)
# light_thread.daemon = True  # 设置为守护线程，主线程结束时自动退出
# light_thread.start()

# @app.route('/api/traffic//traffic_light')
# def get_traffic_light():
#     global traffic_light_color
#     return jsonify({'color': traffic_light_color})

# if __name__ == '__main__':
#     app.run(debug=True,port=5001)

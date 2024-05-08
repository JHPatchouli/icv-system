import json

from flask import Blueprint, Flask, request

import sheet.sheet as sheet

sheet_br=Blueprint('sheet',__name__,template_folder='templates')
def camstream():
    return {'status': '200', 'message': 'success','data': sheet.car_cam_stream()}

def runstatus():
    return {'status': '200', 'message': 'success','data': sheet.cars_run_status()}

def locinfo():
    return {'status': '200', 'message': 'success','data': sheet.car_loc_info()}

def powerstatus():
    return {'status': '200', 'message': 'success','data': sheet.car_power_status()}

def errstatus():
    return {'status': '200', 'message': 'success','data': sheet.car_gy_status()}

def car_ult_data():
    return {'status': '200', 'message': 'success','data': sheet.car_ult_data()}

def camstream_single():
    return {'status': '200', 'message': 'success','data': sheet.car_cam_stream_single()}

def panel_single(panel_id:int,car_id:int):
    if panel_id==1:
        return {'status': '200', 'message': 'success','data': sheet.car_cam_stream_single(car_id)}
    elif panel_id==2:
        return {'status': '200', 'message': 'success','data': sheet.car_loc_info_single(car_id)}
    elif panel_id==3:
        return {'status': '200', 'message': 'success','data': sheet.car_power_status_single(car_id)}
    elif panel_id==4:
        return {'status': '200', 'message': 'success','data': sheet.car_gy_status_single(car_id)}
    return ""

panel_dict={1:camstream,2:runstatus,3:locinfo,4:powerstatus,5:errstatus,6:car_ult_data}
@sheet_br.route('/api/sheet/panel/<int:id>',methods=['GET'])
def panel(id:int):
    selected_function = panel_dict.get(id)
    if selected_function:
        # 如果视图函数需要接收请求对象，则传递请求对象给它
        result = selected_function()  # 假设这里需要传递请求对象
        return json.dumps(result,sort_keys=False)
    else:
        return json.dumps({'status': '404','message': 'Invalid panel ID'}), 404


@sheet_br.route('/api/sheet/panel/<int:panel_id>/<int:car_id>',methods=['GET'])
def panel_s(panel_id:int,car_id:int):
    # return "nihao"
    if(panel_single(panel_id,car_id)==""):
        return json.dumps({'status': '404','message': 'Invalid panel ID'})
    return json.dumps(panel_single(panel_id,car_id),sort_keys=False)
from flask import Flask, request,Blueprint
import json
import sheet.sheet as sheet
sheet_br=Blueprint('sheet',__name__,template_folder='templates')

@sheet_br.route('/api/sheet/run_status/<int:id>',methods=['GET'])
def runstatus(id:int):
    return json.dumps({'status': '200', 'message': 'success','data': sheet.cars_run_status(id)},sort_keys=False)

@sheet_br.route('/api/sheet/cam_stream/<int:id>',methods=['GET'])
def camstream(id:int):
    return json.dumps({'status': '200', 'message': 'success','data': sheet.car_cam_stream(id)},sort_keys=False)

@sheet_br.route('/api/sheet/loc_info/<int:id>',methods=['GET'])
def locinfo(id:int):
    return json.dumps({'status': '200', 'message': 'success','data': sheet.car_loc_info(id)},sort_keys=False)

@sheet_br.route('/api/sheet/ult_data/<int:id>',methods=['GET'])
def ultdata(id:int):
    return json.dumps({'status': '200', 'message': 'success','data': sheet.car_ult_data(id)},sort_keys=False)

@sheet_br.route('/api/sheet/err_status/<int:id>',methods=['GET'])
def errstatus(id:int):
    return json.dumps({'status': '200', 'message': 'success','data': sheet.car_err_status(id)},sort_keys=False)

@sheet_br.route('/api/sheet/power_status/<int:id>',methods=['GET'])
def powerstatus(id:int):
    return json.dumps({'status': '200', 'message': 'success','data': sheet.car_power_status(id)},sort_keys=False)
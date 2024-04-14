import json
from flask import Flask, request,Blueprint
import cards.cards as Obj_Card
cards_br=Blueprint('cards',__name__,template_folder='templates')
#这是一个mysql的cards表所对应Card对象的路由
#可使用对象函数有
# create_card()
# get_card(id)
# get_all_cards()
# update_card(id, raw, r_num, r_ide, r_type, inter_range, over_range, park_range, char_range)
# delete_card(id)

#查询卡片
@cards_br.route('/api/cards/raw/<id>', methods=['GET'])
def get_card_raw(id):
    try:
        card_raw = {'status': 200, 'msg': 'success', 'data': str(Obj_Card.get_card(id).raw)}
        return json.dumps(card_raw, sort_keys=False)
    except:
        card_raw = {'status': 400, 'msg': 'fail', 'data': 'no such card'}
        return json.dumps(card_raw, sort_keys=False)

@cards_br.route('/api/cards/info/<id>', methods=['GET'])
def get_card_info(id):
    try:
        card_info=Obj_Card.get_card(id)
        card_info_dict={'id':card_info.id,'r_num':card_info.r_num,'r_ide': card_info.r_ide,'r_type': card_info.r_type,'inter_range': card_info.inter_range,'over_range': card_info.over_range,'park_range': card_info.park_range,'char_range': card_info.char_range}
        return json.dumps(card_info_dict, sort_keys=False)
    except:
        card_info = {'status': 400, 'msg': 'fail', 'data': 'no such card'}
        return json.dumps(card_info, sort_keys=False)
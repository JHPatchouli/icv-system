from flask import Flask, request, jsonify,Blueprint
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
    card_raw = {'status': 200, 'msg': 'success', 'data': str(Obj_Card.get_card(id).raw)}
    return jsonify(card_raw)
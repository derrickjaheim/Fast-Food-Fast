
from flask import jsonify, request
from flask.views import MethodView

from api.models.views import GetAllOrder


class OrderNow(MethodView):
    user_name = None
    order = None
    order_id= 'order_id'

    def post(self, order_id= None):
        if order_id is None:
           keys = ("user_name", "order","status")

           if not set(keys).issubset(set(request.json)):
                return jsonify({'Blank space': 'Your request has Empty feilds'}), 400

        # self.user_name = request.json['user_name']
        # self.order = request.json['order']

        return jsonify(GetAllOrder.post_order(request.json['user_name'],request.json['user_name'],request.json['order'],request.json['status']))
    def get(self, order_id):
        if order_id is None:
            if GetAllOrder.get_orders is True:
                return jsonify({'message':'no order'})
            return jsonify({'message': GetAllOrder.get_orders(self)})
        return jsonify({'message': GetAllOrder.get_one_order(order_id,order_id)})


    def put(self, counter):
        return jsonify({'orders': GetAllOrder.update_order(counter)}), 201
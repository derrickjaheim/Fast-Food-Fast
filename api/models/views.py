"""end points for the orders"""
from flask import request
from api.models.order import Order

class GetAllOrder:
    """class for getting orders"""
    orders = []

    def __init__(self):
        self.orders = []

    counter = 0

    def post_order(self, user_name, order, status):
        """method for all post orders"""

        self.counter+=1

        order = {'counter': self.counter,'user_name': user_name, 'order': order, 'status': status}
        GetAllOrder.orders.append(order)
        return GetAllOrder.orders

    def get_orders(self):

        if not GetAllOrder.orders:
            return  True
        order_list = [order for order in GetAllOrder.orders]
        return order_list

    def get_one_order(self, order_id):
        for order in GetAllOrder.orders:
            if order_id == order['counter']:
                return order
        return ({'order': 'order_item doesnot exist'}), 200

    def update_order(self, counter):
        if counter:
            for order in GetAllOrder.orders:
                if counter == order['counter']:
                    item_json = request.get_json()
                    status = item_json['status']
                    order['status'] = status

                    return order
        else:
            return "order not found"





if __name__ == '__main__':
    APP.run(debug=True)
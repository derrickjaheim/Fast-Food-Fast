
"""end points for the orders"""
from api.order import Order
from flask import request

class GetAllOrder:
    """class for getting orders"""
    orders = []

    def __init__(self):
        self.orders = []

    def post_order(self, user_name, order):
        """method for all post orders"""

        size = [order for order in GetAllOrder.orders]

        counter = len(size) + 1

        order = { 'counter': counter,'user_name': user_name, 'order': order}
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
        return ({'order': 'order_item doesnot exist'})

    def update_order(self, order_id):
        if order_id:
            for order in GetAllOrder.orders:
                if order_id == order['counter']:
                    item_json = request.get_json()
                    status = item_json['status']
                    order['status'] = status

                    return order
        else:
            return "order item not found"





if __name__ == '__main__':
    APP.run(debug=True)

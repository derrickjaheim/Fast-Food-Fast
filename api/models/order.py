""" Module for orders"""
class Order():
    """
        Class defines the order atributes
        params: user_name, order_id, order
        """
    def __init__(self, counter, user_name, order):
        self.counter = counter
        self.user_name = user_name
        self.order = order
        self.order_status = "pending"

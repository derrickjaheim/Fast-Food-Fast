"""
Module decorates views to urls
"""
from api.controller.main import OrderNow


class GetUrls:
    """
    Method that views with urls
    """
    @staticmethod
    def fetch_urls(order):
        """
        Method that views with urls
        """
        order_view = OrderNow.as_view
        order.add_url_rule('/api/v1/orders/',
                              view_func= order_view('get_all_orders'), defaults={'order_id': None},
                              methods=['GET'])
        order.add_url_rule('/api/v1/orders/<int:order_id>/',
                              view_func= order_view('get_an_order'),
                              methods=['GET'])
        order.add_url_rule('/api/v1/orders/',
                              view_func= order_view('make_orders'), methods=['POST'])

        order.add_url_rule('/api/v1/orders/<int:order_id>/',
                           view_func= order_view('put_an_order'),
                           methods=['PUT'])
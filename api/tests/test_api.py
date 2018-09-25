import unittest
import json

from run import APP

"""
Class for all gets and Post
"""


class TestViews(unittest.TestCase):
    def setUp(self):
        self.order = APP
        self.client = self.order.test_client

    """
    methods defines test cases for get all orders
    """

    def test_get_all_orders(self):
        result = self.client().get('/api/v1/orders/')
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["message"])

    def test_no_orders(self):
        result = self.client().get('/api/v1/orders/1/')
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["message"])

    """
    methods defines test cases for get an order
    """

    def test_get_an_order(self):
        result = self.client().get('/api/v1/orders/2')
        self.assertEqual(result.status_code, 301)

    """
    methods defines test cases for post an order
    """

    def test_post_order(self):
        result = self.client().post('/api/v1/orders/', content_type="application/json", data=json.dumps(
            dict(user_name="Lindsey", order="Burgers", status="")))
        self.assertEqual(result.status_code, 200)



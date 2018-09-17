import unittest
import json

from api.run import APP

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

    def test_getallorders(self):
        result = self.client().get('/api/v1/orders/')
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["message"])

    """
    methods defines test cases for get a question
    """

    def test_getanorder(self):
        result = self.client().get('/api/v1/orders/2')
        self.assertEqual(result.status_code, 301)
        # self.assertTrue(result.json["message"])

    """
    methods defines test cases for post a question
    """

    def test_postorder(self):
        result = self.client().post('/api/v1/orders/', content_type="application/json", data=json.dumps(
            dict(user_name="natasha", order="what is boot camp", )))
        self.assertEqual(result.status_code, 200)
        # self.assertTrue(result.json["orders"])
        # self.assertIn('order', str(result.data))


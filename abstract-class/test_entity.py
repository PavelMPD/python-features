import unittest
from entity import Entity, Order, OrderItem


class TestEntity(unittest.TestCase):
    def setUp(self):
        print("set up")

    def tearDown(self):
        print("tear down")

    def test_order(self):
        order = Order()
        self.assertIsInstance(order, Entity)
        order.save()
        order.delete()

    def test_order_item(self):
        order_item = OrderItem()
        self.assertIsInstance(order_item, Entity)
        order_item.save()
        order_item.delete()

if __name__ == '__main__':
    unittest.main()
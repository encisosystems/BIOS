from django.test import TestCase
from shop.models import *

# Create your tests here.

class TestOrder(TestCase):
    
    def setUp(self):
        Order.objects.create(id=1,complete=True, transaction_id=130)
        self.order= Order.objects.get(transaction_id=130)
        self.queryset = Order.objects.all()

    def test_query_order(self):
        order= self.order.transaction_id
        self.assertEqual(int(order), 130)

    def test_update_order(self):
        self.order.transaction_id = 130
        self.order.save()
        self.assertEqual(self.order.transaction_id, 130)

    def test_delete_order(self):
        self.order.delete()
        self.assertNotIn(self.order, self.queryset)
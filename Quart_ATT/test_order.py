from datetime import datetime

from Entities.Customer import Customer
from Entities.Order import Order
from Entities.OrderProduct import OrderProduct
from Entities.Product import Product
from Repositories.CustomerRepository import CustomerRepository
from Repositories.ProductRepository import ProductRepository
from unittest import mock
import unittest

class TestGera(unittest.TestCase):
    def test_new_order_with_product_total_price(self):

        # ARRANGE
        customer1 = Customer(1, "Flamengo")
        customer_repository = CustomerRepository()
        customer_repository.append_customer(customer1)

        product1 = Product(1, "Nescau", 50, 10)
        product_repository = ProductRepository()
        product_repository.append_product(product1)

        order = Order(1, customer1, datetime.today)
        order_product1 = OrderProduct()
        order_product1.add_product(product1, 5)
        order.add_order_product(order_product1)

        # ACT
        order.update_total_price()

        # ASSERT
        self.assertEqual(order.total_price, 250)

    def test_new_order_without_product(self):
        # Arrange
        customer1 = Customer(1, "Flamengo")
        customer_repository = CustomerRepository()
        customer_repository.append_customer(customer1)

        product1 = Product(1, "Nescau", 50, 10)
        product_repository = ProductRepository()
        product_repository.append_product(product1)

        order = Order(1, customer1, datetime.today)
        order_product1 = OrderProduct()
        order_product1.add_product(product1, 15)
        order.add_order_product(order_product1)

        # ACT
        order.update_total_price()

        # ASSERT
        self.assertEqual(order.total_price, 0)

    def test_process_product_return(self):

        customer1 = Customer(1, "grabiel")
        customer_repository = CustomerRepository()
        customer_repository.append_customer(customer1)

        product1 = Product(1, "leithê", 50, 200)
        product_repository = ProductRepository()
        product_repository.append_product(product1)

        order = Order(1, customer1, datetime.today)
        order_product1 = OrderProduct()
        order_product1.add_product(product1, 10)
        order.add_order_product(order_product1)

        # ACT
        order_product1.process_product(product1, 100)

        # ASSERT

        self.assertEqual(product1.stock,90)

    def test_if_down_stock_is_working(self):

        customer1 = Customer(1, "grabiel")
        customer_repository = CustomerRepository()
        customer_repository.append_customer(customer1)

        product1 = Product(1, "leithê", 50, 200)
        product_repository = ProductRepository()
        product_repository.append_product(product1)

        order = Order(1, customer1, datetime.today)
        order_product1 = OrderProduct()
        order_product1.add_product(product1, 10)
        order.add_order_product(order_product1)

        product1.down_stock(100)

        self.assertEqual(product1.stock,90)
	
	# Criando um novo produto dentro da funcao

    def test_if_down_stock_is_returning_right_stock(self):
        product1 = Product(1, "Milk", 50, 500)
        Estq_actual = 150

        product1.down_stock(a)

        self.assertEqual(product1.stock,100)
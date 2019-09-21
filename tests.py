import unittest
from app import Product


class ProductTest(unittest.TestCase):
    def test_product_stock_can_not_be_less_than_zero(self):
        INVALID_STOCK = [-1, -5, -10000]
        product = Product('Producto 1', 'Descripción del Producto 1')
        for elem in INVALID_STOCK:
            with self.assertRaises(ValueError):
                product.stock = elem

    def test_product_price_can_not_be_less_than_zero(self):
        INVALID_PRICE = [-1, -5, -10000]
        product = Product('Producto 1', 'Descripción del Producto 1')
        for elem in INVALID_PRICE:
            with self.assertRaises(ValueError):
                product.price = elem

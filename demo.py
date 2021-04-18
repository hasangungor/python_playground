from basket import Basket
from product import Product

basket = Basket()
product = Product("Chocolate", 1.99)
basket.add_product(product)
basket.show_product()

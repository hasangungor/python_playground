from product import Product

class Basket:

    product_list = []

    def add_product(self, product):
        self.product_list.append(product)

    def show_product(self):
        print("Product:")
        print("Name: ", self.product_list[0].name)
        print("Price: $", self.product_list[0].price)
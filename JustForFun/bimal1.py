class Sales:
    def __init__(self, sales_no, product_name, product_price, quantity):
        self.sales_no = sales_no
        self.product_name = product_name
        self.product_price = product_price
        self.quantity = quantity
        self.total_sales_price = 0.0

    def get_sales_no(self):
        return self.sales_no

    def set_sales_no(self, sales_no):
        self.sales_no = sales_no

    def get_product_name(self):
        return self.product_name

    def set_product_name(self, product_name):
        self.product_name = product_name

    def get_product_price(self):
        return self.product_price

    def set_product_price(self, product_price):
        self.product_price = product_price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_total_sales_price(self):
        return Sales.calculate_sales_price(self)

    def calculate_sales_price(self):
        if self.quantity > 10:
            self.total_sales_price = self.quantity * self.product_price * 0.95
        else:
            self.total_sales_price = self.quantity * self.product_price
        return self.total_sales_price

    def print_the_values(self):
        print("Sales No:", self.get_sales_no())
        print("Product Name:", self.get_product_name())
        print("Product quantity:", self.get_quantity())
        print("Total Sales Price:", self.get_total_sales_price())


sales_obj = Sales(int(input("Enter the sales no:")), str(input("Enter the product name:")), float(input("Enter the price of the product:")), int(input("Enter the quantity:")))
Sales.set_product_name(sales_obj,sales_obj.product_name)
Sales.set_product_price(sales_obj,sales_obj.product_price)
Sales.set_quantity(sales_obj,sales_obj.quantity)
Sales.set_sales_no(sales_obj,sales_obj.sales_no)
Sales.calculate_sales_price(sales_obj)
Sales.print_the_values(sales_obj)

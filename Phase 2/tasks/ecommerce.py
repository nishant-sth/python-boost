# Your Mission:

# Create a script ecommerce.py.
# Inside, define a Product class.
# The __init__ method should accept name, price, and initial_stock.
# Create a method display() that prints the product's details in a clean format.
# Create a method sell(quantity) that reduces the stock by the given quantity. Add a check to ensure you don't sell more than you have in stock.
# Create a method restock(quantity) that increases the stock.
# Create at least two different product objects (e.g., a "Laptop" and a "Mouse") and test all their methods.

class Product:
    def __init__(self, name:str, price:int, initial_stock:int):
        self.name = name
        self.price = price
        self.initial_stock = initial_stock

    def display(self):
        print('----Product Details----')
        print(f' Name: {self.name} \n Price: {self.price} \n Stock: {self.initial_stock}.')

    def sell(self, quantity):
        print(f'Sell {quantity} {self.name}')
        self.initial_stock-=quantity
        print(f'Remaining stock of {self.name}: {self.initial_stock}')
    
    def restock(self, quantity):
        self.initial_stock+=quantity
        print(f'After adding {quantity} {self.name} - Stock: {self.initial_stock}')

#create two objects 
product1 = Product('Laptop', 134000, 5)
product2 = Product('Mouse', 4500, 10)

#Calling different methods
product1.display()
product1.sell(2)
product1.restock(5)
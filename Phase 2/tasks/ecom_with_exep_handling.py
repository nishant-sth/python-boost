# Your Mission:

# Take your Product class from the first mission in this phase.
# Modify the sell(quantity) method.
# Use a try...except block.
# First, ensure the quantity is an integer. If not, raise a TypeError with a clear message.
# Second, ensure the quantity is a positive number. If not, raise a ValueError.
# The existing check for selling more stock than you have should also be a ValueError.
# Write code outside the class to test these error conditions. For example, try to call my_product.sell("five") or my_product.sell(-1).


class Product:
    def __init__(self, name:str, price:int, initial_stock:int):
        self.name = name
        self.price = price
        self.initial_stock = initial_stock

    def display(self):
        print('----Product Details----')
        print(f' Name: {self.name} \n Price: {self.price} \n Stock: {self.initial_stock}.')

    def sell(self, quantity):
        try:
            #check type
            if isinstance(quantity, str):
                raise TypeError('Quantity cannot be string')
            
            #check negative
            if quantity <= 0:
                raise ValueError("Quantity must be positive number.")
            
            #check stock
            if quantity>self.initial_stock:
                raise ValueError('Not enough stock to complete the sale.')
            
            self.initial_stock-=quantity
            print(f'Sell {quantity} {self.name}')
            print(f'Remaining stock of {self.name}: {self.initial_stock}')
        except (TypeError, ValueError) as e:
            print('Sale Failed.')
            print(f'Error: {e}')
        finally:
            print('Quantity validation complete.')
    
    def restock(self, quantity):
        self.initial_stock+=quantity
        print(f'After adding {quantity} {self.name} - Stock: {self.initial_stock}')

#create two objects 
product1 = Product('Laptop', 134000, 5)
product2 = Product('Mouse', 4500, 10)

#Calling different methods
product1.display()
product1.sell(3)
product1.restock(5)
# Your Mission:

Take your Product class from the first mission in this phase.
Modify the sell(quantity) method.
Use a try...except block.
First, ensure the quantity is an integer. If not, raise a TypeError with a clear message.
Second, ensure the quantity is a positive number. If not, raise a ValueError.
The existing check for selling more stock than you have should also be a ValueError.
Write code outside the class to test these error conditions. For example, try to call my_product.sell("five") or my_product.sell(-1).
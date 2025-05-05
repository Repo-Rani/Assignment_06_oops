# 18. Property Decorators: @property, @setter, and @deleter

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            raise ValueError("Price must be non-negative")

    @price.deleter
    def price(self):
        del self._price

product = Product(100)  
print(product.price)    

product.price = 120   
print(product.price)   

try:
    product.price = -5  
except ValueError as e:
    print(e)          

del product.price    
try:
    print(product.price) 
except AttributeError:
    print("Price attribute deleted") 
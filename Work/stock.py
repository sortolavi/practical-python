
from typedproperty import String, Integer, Float

class Stock:

    # __slots__ = ['name', '_shares', 'price'] # this is an optimization to save memory, but it also prevents adding new attributes to the class

    name = String('name')
    shares = Integer('shares')
    price = Float('price')
  
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares # This assignment calls the setter below
        self.price = price

    # without __repr__, the print of a Stock object is not very informative
    # [<stock.Stock object at 0x0000022C9F7C9FD0>, <stock.Stock object at ...>]

    def __repr__(self):
        return f"Stock({self.name}, {self.shares}, {self.price})"
    

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, cnt):
        self.shares -= cnt

    def buy(self, cnt):
        self.shares += cnt
    
    def update_price(self, price):
        self.price = price



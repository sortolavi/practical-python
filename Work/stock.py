

class Stock:

    __slots__ = ['name', '_shares', 'price'] # this is an optimization to save memory, but it also prevents adding new attributes to the class
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares # This assignment calls the setter below
        self.price = price

    # without __repr__, the print of a Stock object is not very informative
    # [<stock.Stock object at 0x0000022C9F7C9FD0>, <stock.Stock object at ...>]

    def __repr__(self):
        return f"Stock({self.name}, {self.shares}, {self.price})"
    
    # the shares property internally uses a private name, but the rest of the class can use the public name
    # goog.__dict__  gives: {'name': 'GOOG', '_shares': 100, 'price': 490.1}

    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, shares):
        if not isinstance(shares, int) or shares < 0:
            raise ValueError('Shares must be non-negative integer')
        self._shares = shares


    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, cnt):
        self.shares -= cnt

    def buy(self, cnt):
        self.shares += cnt
    
    def update_price(self, price):
        self.price = price



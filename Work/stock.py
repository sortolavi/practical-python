

class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    # without this, the print of a Stock object is not very informative
    # [<stock.Stock object at 0x0000022C9F7C9FD0>, <stock.Stock object at ...>]

    def __repr__(self):
        return f"Stock({self.name}, {self.shares}, {self.price})"

    def cost(self):
        cost = self.shares * self.price
        return cost

    def sell(self, cnt):
        self.shares -= cnt

    def buy(self, cnt):
        self.shares += cnt
    
    def update_price(self, price):
        self.price = price



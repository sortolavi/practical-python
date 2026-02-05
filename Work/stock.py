

class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        cost = self.shares * self.price
        return cost

    def sell(self, cnt):
        self.shares -= cnt

    def buy(self, cnt):
        self.shares += cnt
    
    def update_price(self, price):
        self.price = price



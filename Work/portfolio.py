# portfolio.py

class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self): # usage: for i in object: ...
        return self._holdings.__iter__()
    
    def __len__(self): # usage: len(object)
        return len(self._holdings)

    def __getitem__(self, index): # usage: object[0], object[0:3]
        return self._holdings[index]
    
    def __contains__(self, name): # usage: 'IBM' in object ? True
        # return any([s.name == name for s in self._holdings])
        return any(s.name == name for s in self._holdings)

    
    @property
    def total_cost(self): # usage: object.total_cost
        # return sum([s.shares * s.price for s in self._holdings])
        return sum(s.shares * s.price for s in self._holdings)


    def tabulate_shares(self):
        from collections import Counter

        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares

        return total_shares






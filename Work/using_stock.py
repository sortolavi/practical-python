
import fileparse
import stock


a = stock.Stock('GOOG',100,490.10)

print(a) # Stock(GOOG, 100, 490.1)
print(a.__dict__) # {'name': 'GOOG', '_shares': 100, 'price': 490.1}

columns = ['name', 'shares']
for colname in columns:
        print(colname, '=', getattr(a, colname))
        

b = stock.Stock('AAPL', 50, 122.34)
c = stock.Stock('IBM', 75, 91.75)

print(b.shares * b.price)

stocks = [a, b, c]


for s in stocks:
    print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')

# print(a.cost())
print(a.cost) # because cost is now a property, not a method

a.sell(25)

print(a.shares)
# print(a.cost()) 
print(a.cost) 





# with open ('.\\Data\\portfolio.csv') as lines:
#     portdicts = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])

# print(portdicts)

# portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]

# pf_cost = sum([s.cost() for s in portfolio])
# print (f'Total cost: {pf_cost}')



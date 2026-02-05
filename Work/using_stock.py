
import fileparse
import stock


a = stock.Stock('GOOG',100,490.10)
print(a.name)

b = stock.Stock('AAPL', 50, 122.34)
c = stock.Stock('IBM', 75, 91.75)

print(b.shares * b.price)

stocks = [a, b, c]


for s in stocks:
    print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')

print(a.cost())

a.sell(25)

print(a.shares)
print(a.cost())



with open ('.\\Data\\portfolio.csv') as lines:
    portdicts = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])

print(portdicts)

portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]

pf_cost = sum([s.cost() for s in portfolio])
print (f'Total cost: {pf_cost}')



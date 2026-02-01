
from collections import Counter

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

# combine the shares for each stock
total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += shares

print(total_shares)

# map each stock to a list of (shares, price) tuples
from collections import defaultdict

holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))

print(holdings)



# https://www.geeksforgeeks.org/python/deque-in-python/
# https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque

filename = '.\\Data\\portfolio.csv'
history = deque(maxlen=3)

with open(filename) as f:
    for line in f:
        print(line, end='')  # show the line
        history.append(line)

print('Last 3 lines:')
for line in history:
    print(line, end='')

pf = [{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]

holdings = Counter()

for stock in pf:
    holdings[stock['name']] += int(stock['shares'])

print(holdings)

# report.py
#
# Exercise 2.4 - 2.12
import csv
from pprint import pprint

def read_prices(filename):
    """Reads stock prices from a CSV file and returns a dictionary mapping stock names to prices."""
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        
        for row in rows:
            if not row:  # Skip empty rows
                continue
            
            prices[row[0]] = float(row[1])

    return prices

def read_portfolio(filename):
    """Reads a stock portfolio from a CSV file with handling for missing files."""
    value = 0.0
    data_list = []
    
    try:

      with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows) # skip the header line

        for rownum, row in enumerate(rows, start=2):
            # data_dict = {
            #     'name': row[0],
            #     'shares': int(row[1]),
            #     'price': float(row[2])
            # }
            record = dict(zip(headers, row))
            try:
                record['shares'] = int(record['shares'])
                record['price'] = float(record['price'])
                # value += num_shares * price
                data_list.append(record)

            except ValueError:
                print(f'Line {rownum}: Bad line: {row}')
            
        return data_list, headers
      
    except FileNotFoundError:
      print(f'Error: The file {filename} was not found.')
      return None

def make_report(portfolio, prices):
    """Generates a report of the portfolio with current prices and gain/loss."""
    report = []
    for stock in portfolio:
        name = stock['name']
        shares = int(stock['shares'])
        purchase_price = float(stock['price'])
        current_price = prices.get(name, 0.0)
        gain_loss = (current_price - purchase_price)
        report.append((name, shares, current_price, gain_loss))
    return report


curr_prices = read_prices('.\\Data\\prices.csv')
portfolio = read_portfolio('.\\Data\\portfoliodate.csv')
# print(portfolio[0])
# print(portfolio[1])
pf_data = portfolio[0]
headers = portfolio[1]

report = make_report(pf_data, curr_prices)

for h in headers:
    print('%10s' % h, end=' ')
print()
print(('-' * 10 + ' ') * len(headers))

# for r in report:
#     print('%10s %10d %10.2f %10.2f' % r)

# for name, shares, price, change in report:
#     dollar_price = f'${price:0.2f}'
#     print(f'{name:>10s} {shares:>10d} {dollar_price:>10s} {change:>10.2f}')

for row in pf_data:
    # for i,j in row.items():
    #     print(f'{j:>10s}', end=' ')
    # print()
    for i in list(row.values()):
        print(f'{i:>10}', end=' ')
    print()



    



        







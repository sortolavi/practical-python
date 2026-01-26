# report.py
#
# Exercise 2.4
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
    data_list = []
    
    try:

      with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows) # skip the header line
        for row in rows:
            data_dict = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            data_list.append(data_dict)
        return data_list
      
    except FileNotFoundError:
      print(f'Error: The file {filename} was not found.')
      return None

curr_prices = read_prices('.\\Data\\prices.csv')
portfolio = read_portfolio('.\\Data\\portfolio.csv')
# portfolio = read_portfolio('.\\Data\\missing.csv')

total_cost = 0.0
total_gain_loss = 0.0
curr_value = 0.0

for s in portfolio: # loop through list of dictionaries
    if s['name'] in curr_prices:
       print(f"Updating {s['name']} price from {s['price']} to {curr_prices[s['name']]}")
       s['current_price'] = curr_prices[s['name']]
       s['gain_loss'] = (curr_prices[s['name']] - s['price']) * s['shares']
       curr_value += curr_prices[s['name']] * s['shares']
       
       total_gain_loss += s['gain_loss']
    total_cost += s['shares'] * s['price']

pprint(portfolio)

print(f'Total cost of portfolio: ${total_cost:0.2f} ${total_gain_loss:0.2f} gain/loss  Current value: ${curr_value:0.2f}\n')

for s in portfolio:
   print(f"{s['name']:6s}: {s['shares']:<6} shares at ${s['price']:0.2f}  Current price: ${s['current_price']:<6}  Gain/Loss: ${s['gain_loss']:0.2f}")






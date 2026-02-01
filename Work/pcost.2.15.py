# pcost.py
#
# Exercise 2.15
#
import csv

def portfolio_cost(filename):
    """Calculates the total cost of a stock portfolio from a CSV file with handling for missing files."""
    value = 0.0
    data_list = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)   # take headers from first line

        for linenum, line in enumerate(rows, start=2):
            record = dict(zip(headers, line))
            # print(record)
            try:
                num_shares = int(record['shares'])
                price = float(record['price'])
                value += num_shares * price
                data_list.append(record)
            except ValueError:
                # print(f'Line {linenum}: Bad line: {line.strip()}')
                print(f'Line {linenum}: Bad line: {line}')
            
    # return value
    return data_list
    
      


cost = portfolio_cost('.\\Data\\missing.csv')
# print(f'Total cost of portfolio: ${cost}')
print(cost)


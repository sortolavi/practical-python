# pcost.py
#
# Exercise 2.15
#
import csv

def portfolio_cost(filename, show_errors=False):
    """Calculates the total cost of a stock portfolio from a CSV file with handling for missing files."""
    value = 0.0
    data_list = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)   # take headers from first line

        for linenum, line in enumerate(rows, start=2):
            if not line:    # Skip empty lines
                if show_errors:
                    print(f'Line {linenum}: Empty line')
                continue
            
            types = [str, int, float]

            try:              
                line = [func(val) for func, val in zip(types, line) ]
                
            except ValueError as e:
                if show_errors:
                    # pass
                    print(f'Line {linenum}: Bad line: {line}')
                    print(f'Line {linenum}: Reason: {e}')
                continue
            
            record = dict(zip(headers, line))
            data_list.append(record)
            
    # return value
    return data_list
    
      


pf = portfolio_cost('.\\Data\\missing.csv')
print(pf)

cost = sum([int(i['shares']) * float(i['price']) for i in pf ])
print(f'\nTotal cost of portfolio: ${cost:0.2f}')


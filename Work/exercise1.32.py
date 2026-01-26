import csv

def portfolio_cost(filename):
    """Calculates the total cost of a stock portfolio from a CSV file with handling for missing files."""
    value = 0.0

    try:
      with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows) # skip the header line
        for row in rows:
            itemvalue = int(row[1]) * float(row[2])
            value += itemvalue
            print(f'{row[0]:5s}  ${itemvalue:.2f}')
        return value
    except FileNotFoundError:
      print(f'Error: The file {filename} was not found.')
      return None


cost = portfolio_cost('.\\Data\\portfolio.csv')
# cost = portfolio_cost('.\\Data\\missing.csv')
print(f'Total cost of portfolio: ${cost}')




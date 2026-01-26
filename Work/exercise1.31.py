def portfolio_cost(filename):
    """Calculates the total cost of a stock portfolio from a CSV file with handling for missing files."""
    value = 0.0

    try:
      with open(filename, 'rt') as f:
        headers = next(f).split(',') # skip the header line
        for line in f:
            row = line.split(',')
            itemvalue = int(row[1]) * float(row[2])
            value += itemvalue
            # print(f'{row[0].strip('"'):5s}  {itemvalue:8.2f}')
        return value
    except FileNotFoundError:
      print(f'Error: The file {filename} was not found.')
      return None
    


        

cost = portfolio_cost('.\\Data\\missing.csv')
print(f'Total cost of portfolio: ${cost}')




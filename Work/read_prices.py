import csv

def read_prices(filename):
    """Reads stock prices from a CSV file and returns a dictionary mapping stock names to prices."""
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        
        for row in rows:
            if not row:  # Skip empty rows
                continue
            
            name = row[0]
            price = float(row[1])
            prices[name] = price

    return prices

curr_prices = read_prices('.\\Data\\prices.csv')
print(curr_prices['IBM'])



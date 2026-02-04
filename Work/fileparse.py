# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=True):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)
            start = 2
        else:
            headers = []
            start = 1

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select] # [0, 1 ]
            headers = select
        else:
            indices = []

        records = []
        for rownum, row in enumerate(rows, start=start):
            if not row:    # Skip rows with no data
                continue
            try:
                # Filter the row if specific columns were selected
                if indices:
                    row = [ row[index] for index in indices ]
                
                # Convert types if a list of types is provided
                if types:
                    row = [func(val) for func, val in zip(types, row) ]

            except ValueError as e:
                if not silence_errors:
                  print(f"Row {rownum}: Could not convert: {row}")
                  print(f"Row {rownum}: Reason: {e}\n")
                continue
            
            # print(list(zip(headers, row)))
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records

with open('.\\Data\\portfolio.csv') as f:
    d = parse_csv(f, types=[str, int, float])

print(d)

# portfolio = parse_csv('.\\Data\\portfolio.csv', select=['name','shares'], types=[str, int])
# print(portfolio)

# portfolio = parse_csv('.\\Data\\portfolio.csv', types=[str, int, float])
# print(portfolio)

# prices = parse_csv('.\\Data\\prices.csv', types=[str,float], has_headers=False)
# print(prices)

# portfolio = parse_csv('.\\Data\\portfolio.dat', types=[str, int, float], delimiter=' ')
# print(portfolio)

# portfolio = parse_csv('.\\Data\\portfolio.csv', select=['name','shares'], types=[str, int], has_headers=False)
# print(portfolio)

# portfolio = parse_csv('.\\Data\\missing.csv', types=[str, int, float], silence_errors=False)
# print(portfolio)

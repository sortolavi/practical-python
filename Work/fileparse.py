# fileparse.py
#
# Exercise 3.3
import csv
import gzip

def parse_csv(source, select=None, types=None, has_headers=True, delimiter=',', silence_errors=True):
    '''
    Parse an iterable into a list of records
    '''
    if type(source) == str:
        raise RuntimeError("source must be iterable")
    
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(source, delimiter=delimiter)

    # Read the file headers
    if has_headers:
        headers = next(rows)
        start = 2
    else:
        headers = []
        start = 1

    # If a column selector was given, find those names indices
    # Also narrow the set of headers as given
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



# with open('.\\Data\\portfolio.csv') as f:
#     d = parse_csv(f, types=[str, int, float])

# print(d)



# with gzip.open('.\\Data\\portfolio.csv.gz', 'rt') as f:
#     d = parse_csv(f, types=[str, int, float])

# print(d)



# lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
# pf = parse_csv(lines, types=[str,int,float])
# print(pf)




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

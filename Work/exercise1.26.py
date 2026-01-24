# 1.26
with open('.\\Data\\portfolio.csv', 'rt') as f:
    data = f.read()
    print(data)

with open('.\\Data\\portfolio.csv', 'rt') as f:
    headers = next(f).split(',') # skip the header line
    print('Headers:', headers)
    for line in f:
        row = line.split(',')
        print(row)

# 1.27
# pcost.py

# 1.28
# Including the file mode of 'rt' is critical here. If you forget that, you’ll get byte strings instead of normal text strings.
import gzip
with gzip.open('.\\Data\\portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')

# Data scientists are quick to point out that libraries like Pandas already have a function for reading CSV files.
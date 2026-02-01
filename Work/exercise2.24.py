import csv

types = [str, int, float]

f = open('.\\Data\\portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(row)

print(types[1](row[1])*types[2](row[2]))

r = list(zip(types, row))
# [(<class 'str'>, 'AA'), (<class 'int'>, '100'), (<class 'float'>, '32.20')]

converted = [func(val) for func, val in zip(types, row)] # [str('AA'), int('100'), float('32.20')]
print(converted,'\t' , converted[1] * converted[2])
# ['AA', 100, 32.2]    3220.0000000000005


# { name: func(val) for name, func, val in zip(headers, types, row) }

print(list(zip(headers, types, row))) # [('name', <class 'str'>, 'AA'), ('shares', ... ]

record = { name: func(val) for name, func, val in zip(headers, types, row) }
print(record) # {'name': 'AA', 'shares': 100, 'price': 32.2}


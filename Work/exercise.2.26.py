import csv

f = open('.\\Data\\dowstocks.csv')
rows = csv.reader(f)
headers = next(rows) # ['name', 'price', 'date', 'time', 'change', 'open', 'high', 'low', 'volume']
# row = next(rows) # ['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '39.67', '39.69', '39.45', '181800']

types = [str, float, str, str, float, float, float, float, int]

# record = { name: func(val) for name, func, val in zip(headers, types, row) }
# print(record)
# {'name': 'AA', 'price': 39.48, 'date': '6/11/2007', 'time': '9:36am', 'change': -0.18, 'open': 39.67, 'high': 39.69, 'low': 39.45, 'volume': 181800}

records = [ { name: func(val) for name, func, val in zip(headers, types, row) } for row in rows]
print(records[:3])
# [{'name': 'IBM', 'price': 91.10, 'date': '5/13/2007', 'time': '4:20pm', 'change': 0.56, 'open': 90.54, 'high': 91.20, 'low': 90.50, 'volume': 183900}, {'name': 'CAT', 'price': 83.44, 'date': '9/23/2006', 'time': '1:30pm', 'change': -0.12, 'open': 83.56, 'high': 83.80, 'low': 83.40, 'volume': 121500}, {'name': 'MSFT', 'price': 51.23, 'date': '5/17/2007', 'time': '10:30am', 'change': 0.15, 'open': 51.08, 'high': 51.30, 'low': 51.00, 'volume': 195500}]


for record in records[:3]:
  for name, val in record.items():
      if name == 'date':
          record[name] = tuple(val.split('/'))

    

print(records[:3])






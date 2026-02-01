# extracting data from csv file
'''
name,date,time,shares,price
"AA","6/11/2007","9:50am",100,32.20
"IBM","5/13/2007","4:20pm",50,91.10
"CAT","9/23/2006","1:30pm",150,83.44
"MSFT","5/17/2007","10:30am",200,51.23
"GE","2/1/2006","10:45am",95,40.37
"MSFT","10/31/2006","12:05pm",50,65.10
"IBM","7/9/2006","3:15pm",100,70.44
'''
import csv

f = open('.\\Data\\portfoliodate.csv')
rows = csv.reader(f)
headers = next(rows)
print(headers)
# ['name', 'date', 'time', 'shares', 'price']

selected_rows = ['name', 'shares', 'price']

indices = [headers.index(colname) for colname in selected_rows]
print(indices)
# [0, 3, 4]

# editor.inlineSuggest.enabled set it false, then again true 31.1.2026

row = next(rows)
# turn a row into a dictionary
# zip(selected_rows, indices) -> ('name', 0), ('shares', 3), ('price', 4)
record = { colname: row[index] for colname, index in zip(selected_rows, indices)}
# {'name': 'AA', 'shares': '100', 'price': '32.20'}

portfolio = [ { colname: row[index] for colname, index in zip(selected_rows, indices)} for row in rows]
print(portfolio)

# [{'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': ... ]

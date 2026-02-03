# pcost.py
#
# Exercise 1.27

value = 0.0

with open('.\\Data\\portfolio.csv', 'rt') as f:
    headers = next(f).split(',') # skip the header line
    print('Headers:', headers)
    for line in f:
        row = line.split(',')
        itemvalue = int(row[1]) * float(row[2])
        showvalue = '$' + str(round(itemvalue, 2))
        value += itemvalue
        print(f'{row[0].strip('"'):5s}  {itemvalue:8.2f} {showvalue:10s}')

print(f'Total cost of portfolio: ${value:0.2f}')




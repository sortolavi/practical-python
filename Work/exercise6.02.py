

def countdown(n):
    # Added a print statement
    print('Counting down from', n)
    while n > 0:
        yield n
        n -= 1

def printtaa():
    x = countdown(10)
    print(x)
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())

# printtaa()

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line


from follow import follow

lines = follow('.\\Data\\stocklog.csv')
# ibm = filematch(lines, 'IBM')
# for line in ibm:
#     print(line)

import csv

rows = csv.reader(lines)
for row in rows:
    print(row)


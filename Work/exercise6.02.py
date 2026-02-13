

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

def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line

# for line in open('.\\Data\\portfolio.csv'):
#     print(line, end='')

f = filematch('.\\Data\\portfolio.csv', 'IBM')
# print(f)
# print(f.__next__(), end='')
# print(f.__next__(), end='')

for line in f:
    print(line, end='')


# for line in filematch('.\\Data\\portfolio.csv', 'IBM'):
#     print(line, end='')
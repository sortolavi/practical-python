f = open('foo.txt', 'rt')
g = open('bar.txt', 'wt')

# f.write('some text\n')

data = f.read()

# data = f.read([100]) # read up to 100 bytes

g.write('some text to bar\n')

f.close()
g.close()

with open('foo.txt', 'rt') as f, open('bar.txt', 'wt') as g:
    data = f.read()
    g.write('some more text\n')
    print('Hello, world!', file= g)
    

print(data)

# 1.19
symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
symlist = symbols.split(',')
print(symlist)

symlist[2] = 'AIG'
print(symlist)

mysyms = []
mysyms.append('NOKIA')

symlist[-2:] = mysyms
print(symlist)

# 1.20
for s in symlist:
    print(s)

# 1.21
print('NOKIA' in symlist)
print('DELL' not in symlist)

# 1.22
symlist.append('RHT')
symlist.insert(1,'AA')
symlist.append('YHOO')
print(symlist)

print(symlist.index('YHOO'))
print(symlist.count('YHOO'))
symlist.remove('YHOO')
print(symlist)

# 1.23
symlist.sort()
print(symlist)
symlist.sort(reverse=True)
print(symlist)

# 1.24
a = ', '.join(symlist)

print(a)

# 1.25
nums = [1,2,3,4,5]
items = ['spam', a, nums]
print(items)
print(items[1]) # string a
print(items[2][3]) #4

print(items[1][11:15]) # NOKI


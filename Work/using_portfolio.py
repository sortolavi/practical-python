
import report

portfolio = report.read_portfolio('.\\Data\\portfolio.csv')


print(len(portfolio))

print(portfolio[0])
print(portfolio[1])
print(portfolio[0:3])

print('IBM' in portfolio)
print('YIT' in portfolio)

print(portfolio.total_cost)
holdings = portfolio.tabulate_shares()
print(holdings)

print(holdings.most_common(2))

for h in holdings:
    print(h, holdings[h])



def stock_name(s):
    return 1/s.price # reverse order

portfolio = list(portfolio)

portfolio.sort(key=stock_name)
for s in portfolio:
    print(s)

print()

portfolio.sort(key=lambda s: s.price)
for s in portfolio:
    print(s)

""" 
class Box:
    
    def __init__(self, x=5, y=5):
        self.x = x
        self.y = y

    # def __getattribute__(self, name):
    #     if name == "x":
    #         return 'No access.'
    #     else:
    #         # print(dir(name))
    #         return self

    @property
    def foo(self):
        return self.y

Box.g = 100
b = Box(y=333)

f = b.foo
print(b.x, b.g, f)
# print(Box.__dict__)
 """

"""     
t = (10,20,30)    
for i in range(len(t)):
    print('i:',i)
    print(t[:i], t[i]+i , t[i+1:])
    print('t ennen:',t)
    t = t[:i] + (t[i] + i,) + t[i+1:]
    print('t jälkeen:',t)
    print()
 """
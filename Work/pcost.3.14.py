#
# Exercise 3.14

from report import read_portfolio

def portfolio_cost(filename):
    ''' Calculate total cost of portofolio '''

    portfolio = read_portfolio(filename)
    return sum([i['shares'] * i['price'] for i in portfolio ]) # testing



cost = portfolio_cost('.\\Data\\portfolio.csv') # testing

print(f'Total cost of portfolio: ${cost:0.2f}') # testing


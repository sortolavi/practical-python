#
# Exercise 3.14

from report import read_portfolio

def portfolio_cost(filename):
    ''' Calculate total cost of portofolio 
    
     :param filename: The name of the CSV file containing the portfolio data.
     :return: The total cost of the portfolio as a float.
    '''

    portfolio = read_portfolio(filename) # Portfolio class object
    # return sum([i['shares'] * i['price'] for i in portfolio ])
    # return sum([i.shares * i.price for i in portfolio ])
    return portfolio.total_cost




def main(argv):
    pf_file = argv[1]
    cost = portfolio_cost(pf_file)
    print(f'Total cost of portfolio: ${cost:0.2f}')

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfoliofile')
    
    main(sys.argv)


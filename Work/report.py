# report.py
#
# Exercise 2.4 - 2.12 - 3.16
import csv
from pprint import pprint
from fileparse import parse_csv


def read_prices(filename):
    """Reads stock prices from a CSV file and returns a dictionary mapping stock names to prices."""
    
    with open(filename) as f:
        prices = parse_csv(f, types=[str,float], has_headers=False)
    return dict(prices)

def read_portfolio(filename):
    """Reads a stock portfolio from a CSV file with handling for missing files and returns a list."""
    
    with open(filename) as f:
        portfolio = parse_csv(f, types=[str, int, float])
    return portfolio

def make_report(portfolio, prices):
    """Generates a report of the portfolio with current prices and gain/loss."""
    report = []
    for stock in portfolio:
        name = stock['name']
        shares = int(stock['shares'])
        purchase_price = float(stock['price'])
        current_price = prices.get(name, 0.0) # this is why prices must be a dict, not a list
        gain_loss = (current_price - purchase_price)
        report.append((name, shares, current_price, gain_loss))
    return report

def print_report(report):
    """Prints the report in a formatted manner."""
    print('%10s %10s %10s %10s' % ('Name', 'Shares', 'Price', 'Change'))
    print(('-' * 10 + ' ') * 4)
    for name, shares, price, change in report:
        dollar_price = f'${price:0.2f}'
        print(f'{name:>10s} {shares:>10d} {dollar_price:>10s} {change:>10.2f}')

def portfolio_report(portfolio_file, prices_file):
    """Generates and prints a portfolio report from given files."""

    curr_prices = read_prices(prices_file)
    portfolio = read_portfolio(portfolio_file)
    
    if portfolio is None:
        return  # Exit if portfolio file was not found
    
    report = make_report(portfolio, curr_prices)
    print_report(report)


def main(argv):
    pf_file = argv[1]
    price_file = argv[2]

    portfolio_report(pf_file, price_file)
    

if __name__ == '__main__':
    import sys
    # print('hey this file is executed as main, not imported')
    if len(sys.argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
    
    main(sys.argv)



# report.py
#
# Exercise 3.18 4.4
# import csv
# from pprint import pprint
from fileparse import parse_csv
from portfolio import Portfolio
from stock import Stock
import tableformat


def read_prices(filename):
    """
    Reads stock prices from a CSV file (stockname, price).
    Returns a dictionary mapping stock names to prices.
    """
    
    with open(filename) as f:
        prices = parse_csv(f, types=[str,float], has_headers=False)
    return dict(prices)

def read_portfolio(filename):
    """
    Reads a stock portfolio from a CSV file with handling for missing files.
    Returns a list of Stock objects.
    """
    
    with open(filename) as f:
        portdicts = parse_csv(f, types=[str, int, float])

    portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return Portfolio(portfolio)

def make_report(portfolio, prices):
    '''
    Returns a list of tuples containing (name, shares, current price, gain/loss) for each stock in the portfolio.
    
    :param portfolio: list of Stock objects representing the portfolio
    :param prices: dictionary mapping stock names to current prices
    '''
    report = []
    for stock in portfolio:
        name = stock.name
        shares = int(stock.shares)
        purchase_price = float(stock.price)
        current_price = prices.get(name, 0.0) # this is why prices must be a dict, not a list
        gain_loss = (current_price - purchase_price)
        report.append((name, shares, current_price, gain_loss))
    return report

def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''

    formatter.headings(['Name','Shares','Price ($)','Change ($)'])

    # for name, shares, price, change in reportdata:
    #     dollar_price = f'${price:0.2f}'
    #     print(f'{name:>10s} {shares:>10d} {dollar_price:>10s} {change:>10.2f}')
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfolio_file, prices_file, fmt='txt'):
    '''
    Generates and prints a report of the portfolio with current prices and gain/loss.
    
    :param portfolio_file: a file containing the portfolio data (stock name, shares, purchase price)
    :param prices_file: a file containing the current stock prices (stock name, price)
    '''
    # Read current prices and portfolio data
    curr_prices = read_prices(prices_file)
    portfolio = read_portfolio(portfolio_file)

    if portfolio is None:
        return  # Exit if portfolio file was not found
    
    # Generate the report data
    report = make_report(portfolio, curr_prices)

    # Print the report using a table formatter
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    pf_file = argv[1]
    price_file = argv[2]
    fmt = argv[3] if len(argv) > 3 else 'txt'  # Default to 'txt' if format is not provided
    
    portfolio_report(pf_file, price_file, fmt)
    

if __name__ == '__main__':
    import sys
    # print('this prints when file is executed as main, not imported')
    if len(sys.argv) not in [3, 4]:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile <format>')
    
    main(sys.argv)



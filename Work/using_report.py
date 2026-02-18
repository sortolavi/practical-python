import report as r
import stock

pf_file = '.\\Data\\portfolio.csv'
price_file = '.\\Data\\prices.csv'

# pf_files = ['.\\Data\\portfolio.csv', '.\\Data\\portfolio2.csv'] 
# for file in pf_files:
#     print(f'{file:-^43s}')
#     r.portfolio_report(file, price_file)
#     print()


# read portfolio and print it (just Portfolio object so nothing much to print)
portfolio = r.read_portfolio(pf_file)
print(portfolio)

# make default report with txt formatter
print(f'{pf_file:-^43s}')
r.portfolio_report(pf_file, price_file)
print()

# html formatter
r.portfolio_report(pf_file, price_file, 'html')
print()

# and csv formatter
r.portfolio_report(pf_file, price_file, 'csv')
print()

# r.portfolio_report(pf_file, price_file, 'aku_ankka')
# r.portfolio_report(pf_file)


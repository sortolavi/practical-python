import report as r
import stock


price_file = '.\\Data\\prices.csv'

# pf_files = ['.\\Data\\portfolio.csv', '.\\Data\\portfolio2.csv'] 
# for file in pf_files:
#     print(f'{file:-^43s}')
#     r.portfolio_report(file, price_file)
#     print()

pf_file = '.\\Data\\portfolio.csv'

portfolio = r.read_portfolio(pf_file)
print(portfolio)

print(f'{pf_file:-^43s}')
r.portfolio_report(pf_file, price_file)
print()

r.portfolio_report(pf_file, price_file, 'html')
print()

r.portfolio_report(pf_file, price_file, 'csv')
print()

# r.portfolio_report(pf_file, price_file, 'aku_ankka')


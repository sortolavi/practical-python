import report as r

# pf_files = ['.\\Data\\portfolio.csv', '.\\Data\\portfolio2.csv'] 
price_file = '.\\Data\\prices.csv'

# for file in pf_files:
#     print(f'{file:-^43s}')
#     r.portfolio_report(file, price_file)
#     print()

pf_file = '.\\Data\\portfolio.csv'

print(f'{pf_file:-^43s}')
r.portfolio_report(pf_file, price_file)
print()

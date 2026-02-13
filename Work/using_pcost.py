
from pcost314 import portfolio_cost

# cost = portfolio_cost('.\\Data\\missing.csv')
cost = portfolio_cost('.\\Data\\portfolio.csv')

print(f'Total cost of portfolio: ${cost:0.2f}')


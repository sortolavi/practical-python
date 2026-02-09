

import report as r
import tableformat as tf


pf_file = '.\\Data\\portfolio.csv'

portfolio = r.read_portfolio(pf_file)
formatter = tf.create_formatter('txt')

tf.print_table(portfolio, ['name','shares'], formatter)

tf.print_table(portfolio, ['name','shares','price'], formatter)

tf.print_table(portfolio, ['name','price'], formatter)
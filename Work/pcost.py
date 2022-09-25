# pcost.py
#
# Exercises 1.27, 1.28, and 1.30
import sys
import report

#Checking for a filename given in the command line
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

#Calculating the portfolio cost
portfolio = report.read_portfolio(filename)
cost = sum([s['price']*s['shares'] for s in portfolio])

print('Total cost:', cost)
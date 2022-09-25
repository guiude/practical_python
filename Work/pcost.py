#!/usr/bin/env python3
# pcost.py
#
# Exercises 1.27, 1.28, and 1.30
import report

def main(argv):
    #Checking for a filename given in the command line
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'

    #Calculating the portfolio cost
    portfolio = report.read_portfolio(filename)
    cost = sum([s['price']*s['shares'] for s in portfolio])

    print('Total cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)
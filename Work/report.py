#!/usr/bin/env python3
#report.py

# report.py
#
# Exercise 2.4
from fileparse import parse_csv
import stock
import tableformat
from portfolio import Portfolio

def read_portfolio(filename, **opts):
    '''Returns the content of a portfolio file in a list of dictionaries'''
    with open(filename) as lines:
        portfolio = Portfolio.from_csv(lines)

    return portfolio

def read_prices(filename):
    '''Returns the content of a price file in a dictionary'''
    with open(filename) as lines:
        prices = parse_csv(lines, types=[str,float], has_headers=False)
    return dict(prices)

def calc_portfolio_value(portfolio, prices):
    '''Calculates the current value of a portfolio given a set of prices
       portfolio: a dictionary containing a company name, number of shares, and acquisition value for each share purchase
       prices: a dictionary containing current prices for different equities'''
    current_value = 0
    initial_value = 0

    for company in portfolio:
        curr_price = prices[company.name]
        initial_value += company.cost()
        current_value += company.shares * curr_price
    
    return(current_value, current_value - initial_value)

def make_report(portfolio, prices):
    '''creates the data structure for the performance report'''
    report = []

    for company in portfolio:
        curr_price = prices[company.name]
        gain = curr_price - company.price
        report.append((company.name, company.shares, curr_price, gain))
    
    return report

def print_report(reportdata, formatter):
    '''
    Prints a report in a nicely formatted fashion
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfolio_file, prices_file, fmt='txt'):
    '''
    Prints a portfolio report given portfolio and price files
    fmt indicates the output format and can be txt (default), csv, and html
    '''
    #Read the data from files
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    
    #Assemble the reportdata to be printed
    reportdata = make_report(portfolio, prices)
    
    #Print the report
    formatter = tableformat.create_formatter(fmt)
    print_report(reportdata, formatter)

def main(argv):
    num_args = len(argv)
    if num_args < 3 or num_args > 4:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile pricefile fmt')
    elif num_args == 3:
        portfolio_report(argv[1], argv[2])
    else:
        portfolio_report(argv[1], argv[2], argv[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)
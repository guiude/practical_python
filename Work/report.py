# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv

def read_portfolio(filename):
    '''Returns the content of a portfolio file in a list of dictionaries'''
    portfolio = parse_csv(filename, select=['name','shares','price'], types=[str,int,float])
    return portfolio

def read_prices(filename):
    '''Returns the content of a price file in a dictionary'''
    prices = parse_csv(filename, types=[str,float], has_headers=False)
    return dict(prices)

def calc_portfolio_value(portfolio, prices):
    '''Calculates the current value of a portfolio given a set of prices
       portfolio: a dictionary containing a company name, number of shares, and acquisition value for each share purchase
       prices: a dictionary containing current prices for different equities'''
    current_value = 0
    initial_value = 0

    for company in portfolio:
        curr_price = prices[company['name']]
        initial_value += company['shares'] * company['price']
        current_value += company['shares'] * curr_price
    
    return(current_value, current_value - initial_value)

def make_report(portfolio, prices):
    '''creates the data structure for the performance report'''
    report = []

    for company in portfolio:
        curr_price = prices[company['name']]
        gain = curr_price - company['price']
        report.append((company['name'], company['shares'], curr_price, gain))
    
    return report

def print_report(report):
    '''
    Prints a report in a nicely formatted fashin
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print('---------- ---------- ---------- -----------')
    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

def portfolio_report(portfolio_file, prices_file):
    '''
    Prints a portfolio report given portfolio and price files
    '''
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    report = make_report(portfolio, prices)
    print_report(report)

#time to read the data and prints the report
#'Data/portfoliodate.csv'
#'Data/prices.csv'
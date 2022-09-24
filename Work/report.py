# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    '''Returns the content of a portfolio file in a list of dictionaries'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for num, row in enumerate(rows, start=1):
            try:
                record = dict(zip(headers, row))
                correct_record = {
                    'name': record['name'],
                    'shares': int(record['shares']),
                    'price': float(record['price'])
                }
                portfolio.append(correct_record)
            except ValueError:
                print('Row num: '+ str(num) +'. Bad row: ' + str(row))
    return portfolio

def read_prices(filename):
    '''Returns the content of a price file in a dictionary'''
    f = open(filename, 'r')
    rows = csv.reader(f)
    prices = {}

    for row in rows:
        try:
            prices[row[0]] = float(row[1])
        except IndexError:
            pass 
    return prices

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

#time to read the data and prints the report
portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print('---------- ---------- ---------- -----------')
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)
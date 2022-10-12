#!/usr/bin/env python3
#ticker.py

from .follow import follow
import csv
from . import report
from . import tableformat

def parse_stock_data(lines):
    rows = csv.reader(lines)
    return rows

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfolio_file, log_file, fmt):
    '''
    tracks any change in stocks contained in the portfolio_file that are signaled in log_file
    output produced according to fmt (can be txt, csv, html)
    '''
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['name', 'price', 'change'])

    portfolio = report.read_portfolio(portfolio_file)
    rows = parse_stock_data(follow(log_file))
    rows = (row for row in rows if row['name'] in portfolio)
    for row in rows:
        formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"] )

if __name__ == '__main__':
    portfolio = report.read_portfolio('Data/portfolio.csv')
    rows = parse_stock_data(follow('Data/stocklog.csv'))
    rows = (row for row in rows if row['name'] in portfolio)
    for row in rows:
        print(row)
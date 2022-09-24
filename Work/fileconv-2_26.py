#Exercise 2.26
import os, csv
import pprint


def read_stocks(filename):
    #Opening file
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    row = next(rows)
    portfolio = []

    #Converting using a list of functions/types
    types = [str, float, str, str, float, float, float, float, int]
    for numrow, row in enumerate(rows, start=1):
        try:
            converted = [func(val) for func, val in zip(types, row)]
            record = dict(zip(headers, converted))
            record['parsed_date'] = tuple([int(x) for x in record['date'].split('/')])
            portfolio.append(record)
        except ValueError:
            print('Row num: '+ str(numrow) +'. Bad row: ' + str(row))
    
    return portfolio

#main program
file = 'Data/dowstocks.csv'
portfolio = read_stocks(file)
pprint.pprint(portfolio)
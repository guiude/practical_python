# pcost.py
#
# Exercises 1.27, 1.28, and 1.30
import os, sys

def portfolio_cost(filename):
#Handling potential errors
    try:
        open('Data/' + filename, 'rt')
    except:
        raise RuntimeError('File not found!')
    if filename[-4:] != '.csv': raise RuntimeError('File is not a csv.')

#Executing the function
    with open('Data/' + filename, 'rt') as f:
        headers = next(f).split(',')
        total_cost = 0
        for line in f:
            row = line.split(',')
            try:
                int(row[1])
            except ValueError:
                print('Missing/non-convertible value converted to zero')
                num_shares = 0
                row[1] = 0
            else:
                num_shares = int(row[1])
           
            try:
                float(row[2])
            except ValueError:
                print('Missing/non-convertible value converted to zero')
                total_cost = 0
                row[2] = 0
            else:
                unit_cost = float(row[2])
            total_cost += num_shares*unit_cost
    return total_cost

#Main program
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
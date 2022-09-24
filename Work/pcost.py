# pcost.py
#
# Exercises 1.27, 1.28, and 1.30
import sys, csv

def portfolio_cost(filename):
#Handling potential errors
    try:
        open('Data/' + filename, 'rt')
    except:
        raise RuntimeError('File not found!')
    if filename[-4:] != '.csv': raise RuntimeError('File is not a csv.')

#Executing the function
    with open('Data/' + filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        total_cost = 0
        for num, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                num_shares = int(record['shares'])
                unit_cost = float(record['price'])
                total_cost += num_shares*unit_cost
            except ValueError:
                print('Row num: '+ str(num) +'. Bad row: ' + str(row))
    return total_cost

#Main program
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
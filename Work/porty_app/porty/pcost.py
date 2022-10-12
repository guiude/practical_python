# pcost.py
#
# Exercises 1.27, 1.28, and 1.30
from . import report

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
    
def main(argv):
    #Checking for a filename given in the command line
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'portfolio.csv'
    
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)
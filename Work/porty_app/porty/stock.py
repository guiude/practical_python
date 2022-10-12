from .typedproperty import String, Integer, Float

class Stock:
    '''
    Class to store and manage objects representing stocks in a portfolio
    '''
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    #Method to redefine the Stock object representation
    def __repr__(self) -> str:
        return f'Stock({self.name}, {self.shares}, {self.price})'

    #Method that calculates the stock object cost
    @property
    def cost(self):
        return self.shares * self.price
    
    #Method that sells part of the portfolio
    def sell(self, qty):
        self.shares = max(self.shares - qty, 0)
class Stock:
    #Stock object initiatilization routine
    def __init__(self, name, shares, price):
        self.name = str(name)
        try:
            self.shares = int(shares)
        except ValueError:
            raise RuntimeError('shares in class Stock must be initialized with an int')
        try:
            self.price = float(price)
        except:
            raise RuntimeError('price in class Stock must be initialized with a float')
    
    #Method to redefine the Stock object representation
    def __repr__(self) -> str:
        return f'Stock({self.name}, {self.shares}, {self.price})'

    #Method that calculates the stock object cost
    def cost(self):
        return self.shares * self.price
    
    #Method that sells part of the portfolio
    def sell(self, qty):
        self.shares = max(self.shares - qty, 0)
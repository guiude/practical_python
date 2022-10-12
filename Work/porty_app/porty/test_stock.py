import unittest
from . import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
    
    def test_cost(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, s.shares*s.price)

    def test_sell(self):
        s = stock.Stock('GOOG', 100, 490.1)
        s.sell(25)
        self.assertEqual(s.shares, 100-25)
        s.sell(90)
        self.assertEqual(s.shares, max(100-25-90, 0))

    def test_bad_shares(self):
         s = stock.Stock('GOOG', 100, 490.1)
         with self.assertRaises(TypeError):
             s.shares = '-100'

if __name__ == '__main__':
    unittest.main()
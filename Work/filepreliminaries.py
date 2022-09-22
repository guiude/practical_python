# Exercise 1.26
import os

with open(os.path.dirname(__file__) + '/Data/portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    for line in f:
        row = line.split(',')
        print(row)


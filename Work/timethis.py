#!/usr/bin/env python3
#timethis.py

import time 

def timethis(func):
    '''
    Wrapper to time any function's execution time
    '''
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
    return wrapper

if __name__ == '__main__':
    from sys import argv
    
    num_args = len(argv)

    if num_args != 2:
        raise SystemExit(f'Usage: {argv[0]} ' 'int')
    
    try:
        num=int(argv[1])
    except ValueError:
        raise SystemExit(f'Usage: {argv[0]} ' 'int')

    @timethis
    def countdown(n):
        while n>0:
            n -= 1
    
    countdown(num)
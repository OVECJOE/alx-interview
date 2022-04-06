#!/usr/bin/python3
'''
A module that contain my pascal triangle function
implementation
'''
from functools import reduce


def _combination(n, r):
    '''Compute the combination of r in n.'''
    def n_fac(n):
        '''returns the factorial of n'''
        fac = 1
        for x in range(1, n+1):
            fac *= x
        return fac
    return n_fac(n) // (n_fac(n - r) * n_fac(r))


def pascal_triangle(n):
    '''generates the pascal triangle for a given power'''
    assert type(n) == int
    if n <= 0:
        return []

    return [
        [_combination(x, y) for y in range(x+1)]
        for x in range(1, n+1)
    ]

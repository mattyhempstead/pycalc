import math
import random
import numpy as np
from pathlib import Path

from functools import lru_cache

# 1000 is python default
__import__('sys').setrecursionlimit(100000)


# TODO: Define a help function to print defined util functions


# TODO: Create a wrapper for large numbers
fac=math.factorial

comb=math.comb
perm=math.perm


def mean(a):
    if len(a) == 0:
        raise Exception("Iterable is empty")
    return sum(a)/len(a)


@lru_cache(maxsize=10000)
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@lru_cache(maxsize=10000)
def prime(k:int) -> int:
    """
        Returns the kth prime.

        Calculates the kth prime calculated recursively.
        Get the (k-1)th prime and iterate integers to find the next prime.
    """
    assert k>0
    if k == 1:
        return 2

    # Check for primes starting with previous prime
    check_val = prime(k-1)+1
    while not is_prime(check_val):
        check_val += 1
    return check_val


@lru_cache(maxsize=10000)
def is_prime(n:int, print_factors:bool=False) -> bool:
    """ Returns true if n is prime """
    assert n>0, f"n must be a positive integer: {n}"

    if n == 1:
        return False

    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0:
            if print_factors:
                print(f"Not prime: {i} divides {n}")
            return False
    return True


argmin = np.argmin
argmax = np.argmax

gcd = np.gcd

# LCM(x,y) = x*y / GCD(x,y)
lcm = np.lcm


"""
TODO
 - median
 - mean
 - gcd, gcf, factors
"""



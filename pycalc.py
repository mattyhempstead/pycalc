import math
import random
import numpy as np
from pathlib import Path

from functools import lru_cache

# 1000 is python default
# We import this way to avoid importing the sys module as an object
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
def prime_kth(k:int) -> int:
    """
        Returns the kth prime.

        Calculates the kth prime calculated recursively.
        Get the (k-1)th prime and iterate integers to find the next prime.
    """
    assert k>0
    if k == 1:
        return 2

    # Check for primes starting with previous prime
    check_val = prime_kth(k-1)+1
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


def prime_factors(n):
    """ Returns prime factors of n in a sorted list (with duplicates) """
    factors = []

    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i

    # If n is a prime number greater than 2
    if n > 1:
        factors.append(n)

    return sorted(factors)


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



# Print info about the functions on init
# This seems to be the most usable for me
# (can easily just type ctrl+l)
print("=== pycalc ===")
print("fac - math.factorial")
print("comb - math.comb")
print("perm - math.perm")
print("mean - mean of an iterable")
print("fibonacci - nth fibonacci number")
print("is_prime - boolean of whether n is prime")
print("prime_factors - an increasing list of the prime factors of n (with duplicates)")
print("prime_kth - kth prime number")
print("argmin - index of min value of an iterable")
print("argmax - index of max value of an iterable")
print("gcd - greatest common divisor (factor) of a and b")
print("lcm - least common multiple of a and b")
print()


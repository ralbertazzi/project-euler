import numpy as np

def primes_sieve(max_num):
    
    sieve = np.full(shape=max_num, fill_value=False)
    
    sieve[0] = True
    sieve[1] = True
    sieve[2+2::2] = True
    
    for n in range(3, max_num // 2, 2):
        if sieve[n] == False:
            sieve[n+n::n] = True
            
    return np.where(sieve == False)[0]

def is_prime_trial_division(n):
    
    # From Wikipedia:
    # The simplest primality test is trial division: Given an input number n, 
    # check whether any prime integer m from 2 to sqrt(n) evenly divides n (the division leaves no remainder). 
    # If n is divisible by any m then n is composite, otherwise it is prime.
    
    if n % 2 == 0:
        return False
    
    for d in range(3, int(np.sqrt(n)) + 1):
        if n % d == 0:
            return False
        
    return True

def primality_test_fermat(number):
    return 2**(number - 1) % number == 1


def miller_rabin_base_2(n):
    """Perform the Miller Rabin primality test base 2"""
    d = n-1
    s = 0
    while not d & 1: # Check for divisibility by 2
        d = d >> 1 # Divide by 2 using a binary right shift
        s += 1

    x = pow(2, d, n)
    if x == 1 or x == n-1:
        return True
    for i in range(s-1):
        x = pow(x, 2, n)
        if x == 1:
            return False
        elif x == n - 1:
            return True
    return False
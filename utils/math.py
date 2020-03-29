# gcd and lcm implementations from https://gist.github.com/endolith/114336

# Greatest common divisor of more than 2 numbers.  Am I terrible for doing it this way?

def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return reduce(gcd, numbers)

# Least common multiple is not in standard libraries? It's in gmpy, but this is simple enough:

def lcm(*numbers):
    """Return lowest common multiple."""    
    def _lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(_lcm, numbers, 1)


def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def prod_of_list(l):
    p = 1
    for el in l:
        p = p * el
    return p

def number_from_list_of_digits(l):
    return sum(digit*(10**(len(l) - idx - 1)) for idx, digit in enumerate(l))


def factorial(number):
    
    if number == 0 or number == 1:
        return 1
    else:
        prod = 1
        for el in range(2, number + 1):
            prod *= el
        return prod

    
def proper_divisors(number):
    
    for d in range(1, number // 2 + 1):
        if number % d == 0:
            yield d

            
def fibonacci():
    
    """
    Infinite fibonacci sequence
    """
    
    n1, n2 = 1, 1
    
    yield n1
    yield n2
    
    while True:
        n1, n2 = n2, n1 + n2
        yield n2

        
from numpy import floor, sqrt
        
def sqrt_continued_fraction(D):
    
    """
    Returns the continued fraction of the sqrt of D
    """
    
    R = int(floor(sqrt(D)))
    f = [R]
    
    a, P, Q = R, 0, 1
    
    P = a*Q - P;
    Q = (D - P*P)/Q;
    a = (R + P)/Q;
    f.append(a)
    
    while Q != 1:
        
        P = a*Q - P;
        Q = (D - P*P)/Q;
        a = (R + P)/Q;
        f.append(a)
        
    return f


from fractions import Fraction

def continued_fraction_list_to_fraction(L):

    """
    Returns the fraction corresponding to the lst of terms of a continued fraction
    (computed for example by the sqrt_continued_fraction method)
    """
    
    L = L[::-1]
    f = Fraction(L[0])
    for v in L[1:]:
        f = v + 1 / f
    return f
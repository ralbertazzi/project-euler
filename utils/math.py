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


def factorial(number):
    
    if number == 0 or number == 1:
        return 1
    else:
        prod = 1
        for el in xrange(2, number + 1):
            prod *= el
        return prod

    
def proper_divisors(number):
    
    for d in xrange(1, number // 2 + 1):
        if number % d == 0:
            yield d

            
def fibonacci():
    
    """
    Infinite fibonacci sequence
    """
    
    n1, n2 = 1, 2
    
    yield n1
    yield n2
    
    while True:
        n1, n2 = n2, n1 + n2
        yield n2
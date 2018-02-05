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
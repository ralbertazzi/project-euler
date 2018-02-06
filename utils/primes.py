import numpy as np

def primes_sieve(max_num):
    
    sieve = np.full(shape=max_num, fill_value=False)
    
    sieve[0] = True
    sieve[1] = True
    sieve[2+2::2] = True
    
    for n in xrange(3, max_num, 2):
        if sieve[n] == False:
            sieve[n+n::n] = True
            
    return np.where(sieve == False)[0]
from itertools import islice

def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result
        
        
def take_nth(generator, idx, start=0):
    
    """
        Take the n-th result from a generator
    """
    
    for el_idx, el in enumerate(generator, start=start):
        if el_idx == idx:
            return el
        
        
def take(generator, how_many):
    
    """
    Take the first how_many results from a generator 
    (or less, if the generator won't generate as many results).
    Note that this function is also a generator.
    """
    
    for _, res in zip(xrange(how_many), generator):
        yield res
# Python version = 2.7.1
# Platform = win32

import gmpy
import itertools

def get_primes():
    """Get a list of all 4 digit prime numbers"""
    L = []
    for n in range(1000, 10000):
        if gmpy.is_prime(n) > 0:
            L.append(n)
        else:
            continue
    return L

def isprime(n):
    """Check if a number is prime"""
    if gmpy.is_prime(n) > 0:
        return True
    else:
        return False
    
def get_permutations(i):
    """Get all permutations of a number i"""
    L = []
    y = str(i)
    x = itertools.permutations(y, 4)
    for e in x:
        e1 = ''.join(map(str, e))
        L.append(e1)
    return L

def are_permutations(x, i, i1, i2):
    """Check if arithmetic sequence are permutations
    of each other?"""
    if (str(i1) in x) and (str(i2) in x):
        print "Answer = ", str(i) + str(i1) + str(i2)

def main():
    """Main Program"""
    L = get_primes()
    for i in L:
        for n in range(1, 3331):
            i1 = i + n
            i2 = (i + n) + n
            if isprime(i1) and isprime(i2):
                x = get_permutations(i)
                y = are_permutations(x, i, i1, i2)
            else:
                continue

if __name__ == '__main__':
    main()

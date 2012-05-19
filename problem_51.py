# Python version = 2.7.1
# Platform = win32

import gmpy
import string

def isprime(n):
    """Return True of False - Prime number"""
    if gmpy.is_prime(n):
        return True
    else:
        return False

def prime_list():
    """Create prime number list below 1000000"""
    L = []
    for n in xrange(100, 1000000):
        if isprime(n):
            L.append(n)
    return L

def replace(s1, n):
    """Replace repeating digits"""
    L1 = []
    for i in range(1, 10):
        y = str(i)
        x = s1.replace(n, y)
        L1.append(x)
    return L1
        
def are_prime(x):
    """Check new number for primality"""
    L2 = []
    for number in x:
        if isprime(int(number)):
            L2.append(int(number))
        else:
            continue
    if len(L2) == 8:
        print "L2 = ", L2
        print "YAHOOOO!"
        return True
            
def call_this(s1, k):
    """Intermediate step"""
    for n in s1:
        if n == k:
            x = replace(s1, n)
            if are_prime(x):
                return True
                
def find_duplicates(prime):
    """Find digits that repeat"""
    s = ''
    s1 = str(prime)
    s = s1[0:-1]
    d = {}
    for i in s:
        # Create Dictionary
        d[i] = s.count(i)
    for k, v in d.items():
        if v > 1:
            if call_this(s1, k):
                break
        else:
            continue

def main():
    """Main Program"""
    x = prime_list()
    for prime in x:
        y = find_duplicates(prime)
        
if __name__ == '__main__':
    main()

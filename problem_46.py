# Python version = 2.7.1
# Platform = win32

import gmpy

def get_primes():
    """Get primes up to 10000"""
    L = []
    for n in range(1, 10000, 2):
        if gmpy.is_prime(n) > 0:
            L.append(n)
    return L

def compute_conject(x, c):
    """Try the conjecture formula"""
    for n in range(1, 100):
        for ii in x:
            conject = ii + (2 * (n ** 2))
            if conject == c:
                return True
            else:
                continue
    return False
        
def main():
    """Main Program"""
    x = get_primes()
    composites = []
    for y in range(1, 10000, 2):
        # make composites up to 10000
        if y not in x:
            composites.append(y)
        else:
            continue
    for c in composites:
        if c > 33:
        # We already know up through 33
            x2 = compute_conject(x, c)
            if x2 == False:
                """print the first odd composite that cannot
                be written as the sum of a prime and twice the square"""
                print "Answer = ", c
                break
            else:
                continue
        else:
            continue
        
if __name__ == '__main__':
    main()

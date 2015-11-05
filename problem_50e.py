# Python version = 2.7.1
# Platform = win32

import gmpy2

def isprime(n):
    """Return True of False - Prime number"""
    if gmpy2.is_prime(n):
        return True
    else:
        return False

def prime_list():
    """Create prime number list below 1000000"""
    L = []
    for n in xrange(1, 1000000):
        if isprime(n):
            L.append(n)
    return L

def add_primes(primes, switch):
    """Return the last number in the list (largest prime),
    and the in-loop counter (consecutive numbers)"""
    counter = switch # start with this prime number
    in_counter = 0
    sum = 0
    L = []
    while sum < 1000000:
        sum = sum + primes[counter]
        if isprime(sum):
            L.append(sum)
        in_counter += 1 # in loop counter
        counter += 1
    if L[-1] < 1000000:
        return L[-1], in_counter
    elif L[-1] > 1000000:
        print "****"
        return L[-2], in_counter
       
def main():
    """Main Program"""
    primes = prime_list()
    main_counter = 0
    for switch in range(0, 20):
        x = add_primes(primes, switch)
        print x[0], x[1]
        if x[0] > main_counter:
            main_counter = x[0]
    print "Answer = ", main_counter
            
if __name__ == '__main__':
    main()

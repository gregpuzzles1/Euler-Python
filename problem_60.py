# Python version = 3.1.3
# Platform = win32

import gmpy
import time

def isprime(n):
    if gmpy.is_prime(n):
        return True
    else:
        return False

def primes_1000():
    L = []
    for i in range(1, 1001):
        if isprime(i):
            L.append(i)
        else:
            continue
    return L

def concat(L):
    L1 = []
    for prime1 in L:
        y = str(prime1)
        for prime in L:
            z = str(prime)
            yz = y + z
            zy = z + y
            if isprime(int(yz)) and isprime(int(zy)):
                print (prime1, prime, yz, zy)
                L1.append(yz)
                L1.append(zy)
            else:
                continue
    return L1
            
def main():
    start_time = time.clock()
    a = primes_1000()
    b = concat(a)
    #for i in b:
        #print (i)

    run_time = time.clock() - start_time
    print (run_time)

if __name__ == '__main__':
    main()

# Python version 2.7.2
# Platform = win32

def isprime(n):
    """Checks number (n) for primality, and returns
    True of False."""
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True 

def main():
    """this example takes the numbers 1, 3, 5, 7, 9, etc., and
    checks for primality."""
    Switch = 1
    number = 1
    primes = 1 # start with 1 since we do not count 2, which is a prime
    while Switch == 1:
        if isprime(number):
            primes += 1 
        if primes == 10001: # Stop at 10001, and print that number
            print number
            Switch = 0
        number += 2

if __name__ == '__main__':
    main()

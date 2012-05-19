# Python version = 2.7.1
# Platform = win32

from __future__ import division
import gmpy

def isprime(n):
    """Return True of False - Prime Number"""
    if gmpy.is_prime(n):
        return True
    else:
        return False

def form_diagonal(passed):
    """Form a leg of the diagonal, return the
    number of primes in that leg, and (i), which
    is 1/2 the length of the diagonal."""
    summer = 1
    adder = 0
    L = []
    for i in range(1, 13120): # 1/2 the length of the diagonal
        if i < 2:
            adder = passed
        else:
            adder = adder + 8
        summer = summer + adder
        if isprime(summer):
            L.append(summer)
    return len(L), i
        
def main():
    """Main Program"""
    upper_right = form_diagonal(2)
    upper_left = form_diagonal(4)
    lower_left = form_diagonal(6)
    lower_right = form_diagonal(8)
    primes = upper_right[0] + upper_left[0] + \
             lower_left[0] + lower_right[0]
    all_numbers = (lower_right[1] * 4) + 1
    ratio = primes / all_numbers
    print ("ratio = ", ratio)
    if ratio < .10:
        print ("Ratio is less than 10%")
    
if __name__ == '__main__':
    main()

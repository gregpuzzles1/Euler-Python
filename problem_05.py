# Python Version = 2.7.2
# Platform = win32
# Run time =  0.442848859867

import time

def evenlyDivisible(n):
    """Checks if number (n) is evenly divisible by the numbers 1 -20."""
    counter = 0
    for i in range(1, 21):
        if n % i == 0:
            counter = counter + 1
            if counter == 20:
                return n
        else:
            return 1

def main():
    """Main program - since we know that 2520 is evenly divisible by
    the first 10 integers, we know that the number in question is a
    multiple of 2520. So we start with 2520 and increment by that much
    until we find the smallest number that is evenly divisible by the
    first 20 integers (1-20)"""
    start_time = time.clock()
    n = 2520
    switch = 1
    while switch == 1:
        smallest = evenlyDivisible(n)
        if smallest != 1:
            print smallest
            switch = 0
        else:
            n += 2520
    run_time = time.clock() - start_time
    print "Run time = ", run_time
    
if __name__ == '__main__':
    main()

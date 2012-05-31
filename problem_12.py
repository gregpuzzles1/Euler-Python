# Python version = 2.7.2
# Platform = win32
# Run time =  16.4755609827 seconds

import math
import time

def factors(n):
    """Returns a set of all the factors of a triangle number (n)."""
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))
    
def main():
    """Main program"""
    start_time = time.clock()
    counter = 0         # Initialise counter for natural numbers
    TriangleNumber = 0  # Initialise triangle number variable
    switch = True       # Switch for while loop
    while switch == True:
        counter += 1
        TriangleNumber += counter               # Get the current triangle number.
        if len(factors(TriangleNumber)) > 500:  # Find all the factors of TriangleNumber,
            switch = False                      # if greater than 500 stop the while loop
    print(TriangleNumber)                       # and print the last triangle number.
    run_time = time.clock() - start_time
    print "Run time = ", run_time
        
if __name__ == '__main__':
    main()

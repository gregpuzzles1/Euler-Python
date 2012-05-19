# Python version = 2.7.2
# Platform = win32

import math

def factors(n):
    """Returns a set of all the factors of a triangle number (n)."""
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))
    
def main():
    """Main program"""
    counter = 0     # Couter for natural numbers
    L = []          # List for summing triangle numbers
    switch = True   # Switch for while loop
    while switch == True:
        counter += 1
        L.append(counter)
        TriangleNumber = sum(L)
        if len(factors(TriangleNumber)) > 500: # Find all the factors of TriangleNumber, 
            switch = False                     # if greater than 500 stop the while loop
    print(TriangleNumber)                      # and print the last triangle number.
        
if __name__ == '__main__':
    main()

# Python version = 2.7.2
# Platform = win32

import math
import time

def sum_factorials(number):
    """Sum the factorials of each integer in a number."""
    number = list(str(number))
    sum_of_factorials = 0
    for integer in number:
        factorial = math.factorial(int(integer))
        sum_of_factorials = sum_of_factorials + factorial
    return sum_of_factorials

def main():
    """Main Program"""
    start_time = time.clock()
    longest_chain = 0
    number_of_chains = 0
    for number in range(66, 1000001):
        counter = 1
        switch = 1
        chain_element = number
        chainList = [number]
        while switch == 1:
            if chain_element not in chainList:
                chainList.append(chain_element)
                counter += 1
            else:
                switch = 0
        if counter > longest_chain:
            #if counter == longest_chain:
                #number_of_chains += 1
            longest_chain = counter
            print "longest chain now = ", longest_chain
    print "longest_chain = ", longest_chain
    run_time = time.clock() - start_time
    print "Run time = ", run_time
            

if __name__ == '__main__':
    main()

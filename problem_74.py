# Python version = 2.7.2
# Platform = win32

import math
import time

def factorials_dict():
    """Create a dictionary of factorials 0 - 9"""
    d = {}
    for i in xrange(0, 10):
        d[i] = math.factorial(i)
    return d

def main():
    """Main Program"""
    start_time = time.clock()
    longest_chain = 0
    number_of_chains = 0
    factorials = factorials_dict()
    for number in xrange(66, 1000001):
        counter = 1
        switch = 1
        chain_element = number
        chainList = [number]
        chainList = set(chainList)
        while switch == 1:
            chain_element = str(chain_element)
            sum_factorials = 0
            for integer in chain_element:
                sum_factorials = factorials[int(integer)] + sum_factorials
            chain_element = sum_factorials
            if chain_element not in chainList:
                chainList.add(chain_element)
                counter += 1
            else:
                switch = 0
        if counter > longest_chain:
            number_of_chains = 1
            longest_chain = counter
        elif counter == longest_chain:
            number_of_chains += 1
        else:
            continue
    print "longest_chain = ", longest_chain
    print "number_of_chains = ", number_of_chains
    run_time = time.clock() - start_time
    print "Run time = ", run_time
            
if __name__ == '__main__':
    main()

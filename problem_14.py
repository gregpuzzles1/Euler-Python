# Python version = 2.7.2
# Platform = win32

import time

def main():
    """Main Program"""
    start_time = time.clock()
    largest = 0
    longest_sequence = 0
    Cache = dict()
    for n in xrange(2, 1000001):
        Number = n
        counter = 0
        while Number > 1:
            try:
                counter += Cache[Number] - 1
                break
            except KeyError:
                pass
            
            if Number % 2 == 0:
                Number = Number / 2
            else:
                Number = Number * 3 + 1
            counter += 1

        counter += 1
        Cache[n] = counter

        if counter > longest_sequence:
            longest_sequence = counter
            largest = n

    print "Answer = %s" % largest
    print "longest sequence = %s" % longest_sequence
    
    run_time = time.clock() - start_time
    print "Run time = ", run_time
        
if __name__ == '__main__':
    main()

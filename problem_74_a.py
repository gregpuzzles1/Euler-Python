# Python version = 2.7.2
# Platform = win32

import math
import time

def factorials_dict():
    d = {}
    for i in xrange(0, 10):
        d[i] = math.factorial(i)
    return d

def main():
    dictionary = factorials_dict()
    for number in xrange(66, 150):
        number = str(number)
        sum_factorials = 0
        for integer in number:
            sum_factorials = dictionary[int(integer)] + sum_factorials
        print "sum_factorials = ", sum_factorials

if __name__ == '__main__':
    main()

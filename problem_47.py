# Python version = 2.7.1
# Platform = win32
# stop_time =  6.33370859353 (seconds)

import sympy
import time
    
def get_factors(n):
    """Factor number n"""
    f = sympy.factorint(n)
    return f
        
def main():
    """Main Program"""
    start_time = time.clock()
    counter = 0
    for n in range(1000, 1000000):
        if counter == 4:
            print "Answer=", n - 4
            break
        else:
            x = get_factors(n)
            if len(x) == 4:
                counter += 1
            else:
                counter = 0
    stop_time = time.clock() - start_time
    print "stop_time = ", stop_time
    
if __name__ == '__main__':
    main()

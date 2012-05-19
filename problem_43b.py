# Python version = 2.7.1
# Platform = win32
"""run_time was 36 seconds"""

import itertools
import time

def get_divisibles(s):
    """Get the 7 divisibles"""
    x = list(str(s))
    L = []
    for i in xrange(1, 8):
        d = x[i] + x[i + 1] + x[i + 2]
        L.append(d)
    return L

def isdivisible(y, LL):
    """Check the 7 divisibles"""
    if int(y[0]) % int(LL[0]) == 0 and int(y[1]) % int(LL[1]) == 0 \
       and int(y[2]) % int(LL[2]) == 0 and int(y[3]) % int(LL[3]) == 0 \
       and int(y[4]) % int(LL[4]) == 0 and int(y[5]) % int(LL[5]) == 0 \
       and int(y[6]) % int(LL[6]) == 0:
        return True
    else:
        return False

def main():
    """Main Program"""
    start_time = time.time()
    summer = 0
    x = itertools.permutations('0123456789', 10)
    for n in x:
        s = ''.join(n)
        y = get_divisibles(s)
        LL = [2, 3, 5, 7, 11, 13, 17]
        z = isdivisible(y, LL)
        if z == True:
            summer = summer + int(s)
        else:
            continue
    print "Answer = ", summer
    stop_time = time.time()
    run_time = stop_time - start_time
    print "run_time = ", run_time
        
if __name__ == '__main__':
    main()

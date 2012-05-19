# Python version = 2.7.1
# Platform = win32

from __future__ import division
import math

def main():
    """Main Program"""
    p = set(n * ((3 * n) - 1) / 2 for n in range(2, 4000))
    for i in p:
        for j in p:
            if i + j in p and j - i in p:
                x = i - j
            else:
                continue
    print "Answer = ", math.fabs(x)
    """Answer is the first vaule of x, as the
    pentagonal numbers get larger, they get farther
    apart, makes some sense..."""

if __name__ == '__main__':
    main()

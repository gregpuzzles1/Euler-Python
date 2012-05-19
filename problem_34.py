# Python version = 2.7.1
# Platform is win32

def factorial(L):
    """Get the factorials"""
    sum_factorial = 0
    for i in L:
        fact = 1
        for j in range(1, (int(i) + 1)):
            fact = fact * j
        sum_factorial = sum_factorial + fact
    return sum_factorial

def main():
    """Main Program"""
    L = []
    LN = []
    for n in range(1, 1000001):
        L = list(str(n))
        x = factorial(L)
        if x == n:
            LN.append(n)
    y = sum(LN)
    print "LN = ", LN
    print "Answer = ", y - 3
    # subract 3 for 1! and 2!

if __name__ == '__main__':
    main()

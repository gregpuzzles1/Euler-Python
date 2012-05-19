# Python version = 2.7.1
# Platform = win32

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n 
    # for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def ispandigital(n):
    """Check if integer n is pandigital"""
    x = list(str(n))
    L = []
    for i in x:
        if i not in L:
            L.append(i)
        else:
            return False
    return True

def main():
    """Main Program"""
    largest = 0
    for n in range(1000000, 10000000):
        if isprime(n) == True:
            if ispandigital(n) == True:
                if largest < n:
                    largest = n
                else:
                    continue
            else:
                continue
        else:
            continue
    print "Answer = ", largest
                
if __name__ == '__main__':
    main()

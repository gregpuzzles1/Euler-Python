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

def new_rotation(y, n):
    """Checks the rotation of each prime number
    for primes"""
    c = 0
    while n != c:
        j = y[1:]
        r = y[0]
        j.append(r)
        s = ''.join(j)
        c = int(s)
        if isprime(c):
            pass
        else:
            return "False"
        y = list(str(s))
    return "True"

def main():
    """Main Program"""
    L = []
    for n in range(10, 1000000):
        if isprime(n):
            y = list(str(n))
            if new_rotation(y, n) == "True":
                L.append(n)
            else:
                continue
    print "len(L) = ", len(L) + 4
    # add 4 to the total (manually add prime 2, 3, 5, and 7)
    print L
            
if __name__ == '__main__':
    main()

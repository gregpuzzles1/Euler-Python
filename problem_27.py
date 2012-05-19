import math

def isprime(n1):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n1 = abs(int(n1))
    # 0 and 1 are not primes
    if n1 < 2:
        return False
    # 2 is the only even prime number
    if n1 == 2:
        return True
    # all other even numbers are not primes
    if not n1 & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n1**0.5)+1, 2):
        if n1 % x == 0:
            return False
    return True

def primes_up_to(n2): 
    nroot = int(math.sqrt(n2)) 
    sieve = [True] * (n2+1)# range(n2+1) 
    sieve[0] = False 
    sieve[1] = False 
 
    for i in xrange(2, nroot+1): 
        if sieve[i]: 
            m = n2/i - i 
            sieve[i*i: n2+1:i] = [False] * (m+1) 
 
    return [i for i in xrange(n2+1) if sieve[i]]

                
def find_quadratic():
    max1 = 0
    for a in range(-999,1000,2):
        for b in primes_up_to(1000):
            n = 1
            while isprime((n**2)+(a*n)+b):
                n += 1
            if n > max1:
                product = a*b
                max1 = n
    return product
                    
                    

def main():
    print isprime(126479)
    x = set(primes_up_to(1610))
    y = find_quadratic()
    print "product = ", y
    

if __name__ == '__main__':
    main()

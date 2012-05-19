# Python version = 2.7.2
# Platform = win32

def primes(n):
    """Prime number generator up to n - (generates a list)"""
    ## {{{ http://code.activestate.com/recipes/366178/ (r5)
    if n == 2: return [2]
    elif n < 2: return []
    s = range(3, n + 1, 2)
    mroot = n ** 0.5
    half = (n + 1) / 2 - 1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3) / 2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i + 1
        m = 2 * i + 3
    return [2]+[x for x in s if x]

   ## end of http://code.activestate.com/recipes/366178/ }}}

def main():
    """Main Program"""
    print "Sum of all the primes below two million = %d" % sum(primes(2000000))

if __name__ == '__main__':
    main()

# Python version = 2.7.1
# Platform = win32

import time

def create_cubes():
    """Create a set of cubes"""
    L = []
    for c in range(1, 20000):
        cube = pow(c, 3)
        L.append(cube)
    return set(L)

def main():
    """Main program"""
    start_time = time.clock()
    cc = create_cubes()
    for n in cc:
        cbe = str(n)
        cbe = sorted(list(cbe))
        L = []
        for m in cc:
            cpr = str(m)
            cpr = sorted(list(cpr))
            if cpr == cbe:
                L.append(m)
        if len(L) == 5:
            print L
            print "\n"
            break
        else:
            continue
    run_time = time.clock() - start_time
    print "Run time = ", run_time

if __name__ == '__main__':
    main()

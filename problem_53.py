# Python version = 2.7.1
# Platform = win32

import gmpy

def main():
    """Main Program"""
    counter = 0
    for n in range(1, 101):
        for r in range(1, n):
            c = gmpy.comb(n, r)
            if c > 1000000:
                counter += 1
    print counter

if __name__ == '__main__':
    main()

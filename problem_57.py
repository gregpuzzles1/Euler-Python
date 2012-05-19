# Python version = 2.7.1
# Platform = win32

import fractions

def root_two(iterations):
    d = fractions.Fraction(1/2)
    for i in range(iterations):
        d = fractions.Fraction(1/(2+d))
        yield 1 + d


def main():
    for i in root_two(20):
        print i
        

if __name__ == '__main__':
    main()

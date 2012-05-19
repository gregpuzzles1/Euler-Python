import math
    
def main():
    """Main program"""
    for n in xrange(1, 500):
        for m in xrange(n + 1, 500):
            a = int(math.pow(m, 2) - math.pow(n, 2))
            b = 2 * m * n
            c = int(math.pow(m, 2) + math.pow(n, 2))
            if a + b + c == 1000:
                product = a * b * c
                print "a = %d, b = %d, c = %d" % (a, b, c)
    print "Product = %d" % (product)

if __name__ == '__main__':
    main()

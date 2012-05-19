def find_fibonacci(n):
    """Find fibonacci"""
    a, b = 0, 1
    for i in range(0, n):
        x = str(a)
        if len(x) == 1000:
            print a
            print "F(n) = ", i
            break
        a, b, = b, a + b

def main():
    """Main program"""
    n = input("\nHow many numbers of the sequence would you like? ")
    find_fibonacci(n)
    
if __name__ == '__main__':
    main()

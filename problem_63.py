# Python version = 2.7.2
# Platform = win32

def main():
    """Main program - Check all reasonable possibilities"""
    L = []
    for n in range(1, 101):
        for p in range(1, 101):
            x = pow(n, p)
            x = str(x)
            if len(x) == p:
                L.append(p)
                print x
    print "Answer = ", len(L)

if __name__ == '__main__':
    main()

# Python version = 2.7.1
# Platform = win32

def main():
    """Main Program"""
    total = 0
    tally = ''
    for i in range(1, 1001):
        total = total + (i ** i)
    x = str(total)
    y = len(x) - 10
    s = x[y:]
    print "Answer = ", s
    
if __name__ == '__main__':
    main()

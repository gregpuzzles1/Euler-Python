# Python version = 2.7.1
# Platform = win32

def main():
    """Main Program"""
    T = set((n * (n + 1) / 2) for n in range(2, 180000))
    P = set((n * ((3 * n) - 1) / 2) for n in range(2, 180000))
    H = set((n * ((2 * n) - 1)) for n in range(2, 180000))
    for i in T:
        if i in P and i in H:
            print "You found one"
            print i
        else:
            continue

if __name__ == '__main__':
    main()

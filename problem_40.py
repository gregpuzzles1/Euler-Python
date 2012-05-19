# Python version = 2.7.1
# Platform = win32

def main():
    """Main Program"""
    x = ''
    for n in range(1000000):
        x = x + str(n)
        if len(x) > 1000000:
            break
        else:
            continue
    Answer = int(x[1]) * int(x[10]) * int(x[100]) \
             * int(x[1000]) * int(x[10000]) * \
             int(x[100000]) * int(x[1000000])
    print "Answer = ", Answer

if __name__ == '__main__':
    main()

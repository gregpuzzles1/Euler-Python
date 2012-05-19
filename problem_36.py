# Python version = 2.7.1
# Platform = win32

def binary_rep(i):
    """Take decimal i and convert to binary with
    built in function bin, slice off first two
    characters."""
    x = bin(i)
    y = x[2:]
    return y

def reverse_binary(y):
    """Take binary number y and reverse characters"""
    x = y[::-1]
    return x

def reverse_decimal(i):
    """Take decimal number i and reverse characters"""
    y = str(i)
    d = y[::-1]
    return d

def main():
    """Main Program"""
    L = []
    Answer = 0
    for i in range(1, 1000000):
        x = binary_rep(i)
        y = reverse_binary(x)
        if x == y:
            a = int(reverse_decimal(i))
            if i == a:
                L.append(i)
        else:
            continue
    Answer = sum(L)
    print "Sum = ", Answer
        
if __name__ == '__main__':
    main()

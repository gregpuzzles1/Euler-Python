# Python version = 2.7.1
# Platform = win32

def find_length(L):
    """Find the length of the items
    in the list L (is it == 9?)"""
    x = 0
    for i in L:
        x = x + len(str(i))
    return x

def ispandigital(L):
    """Is the 9 digit number pandigital"""
    concat = ''
    L1 = []
    for i in L:
        x = str(i)
        concat += x
    for b in concat:
        if b not in L1:
            if b != '0':
                L1.append(b)
            else:
                return "False"
        else:
            return "False"
    return "True", concat
    
def main():
    """Main Program"""
    largest = 0
    for i in range(1, 10000):
        L = []
        for y in range(1, 10):
            x = i * y
            if x not in L:
                L.append(x)
                c = find_length(L)
                if c == 9:
                    k = ispandigital(L)
                    if k[0] == "True":
                        if largest < k[1]:
                            largest = k[1]
                        else:
                            continue
                    else:
                        continue
                elif c > 9:
                    break
                else:
                    continue
            else:
                print "Error Message"
    print "Answer = ", largest
        
if __name__ == '__main__':
    main()

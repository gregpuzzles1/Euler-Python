def factor(number):
    """Factor a numer"""
    L = []
    for i in range(1, ((number / 2) + 1)):
        if number%i == 0:
            L.append(i)
    return L

def get_total(x):
    """Total the elements in list L"""
    total = sum(x)
    return total

def main():
    """Main program"""
    tally = 0 
    for y in range(1, 10001):
        x = factor(y) # A list
        x1 = get_total(x)
        x3 = factor(x1) # A list
        x4 = get_total(x3)
        if (y == x4) and (y != x1):
            tally = tally + y
            print "tally = %s y = %s" % (tally, y)
    print "Final Tally = %s" % tally
            
if __name__ == '__main__':
    main()

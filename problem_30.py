def split_number(x):
    """Split number x into a list yy of individual numbers"""
    yy = list(str(x))
    return yy

def sum_of_powers(x, y, length_y):
    """Find the sum of the individual numbers raised to the 5th power
    and determine if they are equal to x"""
    x1, x2, x3, x4, x5, x6 = 0, 0, 0, 0, 0, 0
    if length_y == 1:
        x1 = int(y[0]) ** 5
        if x1 == x:
            return "True"
        else:
            return "False"
    elif length_y == 2:
        x1 = int(y[0]) ** 5
        x2 = int(y[1]) ** 5
        if x1 + x2 == x:
            return "True"
        else:
            return "False"
    elif length_y == 3:
        x1 = int(y[0]) ** 5
        x2 = int(y[1]) ** 5
        x3 = int(y[2]) ** 5
        if x1 + x2 + x3 == x:
            return "True"
        else:
            return "False"
    elif length_y == 4:
        x1 = int(y[0]) ** 5
        x2 = int(y[1]) ** 5
        x3 = int(y[2]) ** 5
        x4 = int(y[3]) ** 5
        if x1 + x2 + x3 + x4 == x:
            return "True"
        else:
            return "False"
    elif length_y == 5:
        x1 = int(y[0]) ** 5
        x2 = int(y[1]) ** 5
        x3 = int(y[2]) ** 5
        x4 = int(y[3]) ** 5
        x5 = int(y[4]) ** 5
        if x1 + x2 + x3 + x4 + x5 == x:
            return "True"
        else:
            return "False"
    elif length_y == 6:
        x1 = int(y[0]) ** 5
        x2 = int(y[1]) ** 5
        x3 = int(y[2]) ** 5
        x4 = int(y[3]) ** 5
        x5 = int(y[4]) ** 5
        x6 = int(y[5]) ** 5
        if x1 + x2 + x3 + x4 + x5 + x6 == x:
            return "True"
        else:
            return "False"
    else:
        print "Error Message"
        
def main():
    """Main Program"""
    L = []
    for x in range(2, 1000000):
        y = split_number(x)
        length_y = len(y)
        xy = sum_of_powers(x, y, length_y)
        if xy == 'False':
            pass
        else:
            L.append(x)
    print "L = ", L
    print "Sum of list L = ", sum(L)

if __name__ == '__main__':
    main()

def twos():
    """Return a set of two digit numbers that
    do not repeat or have a zero in them"""
    twos = []
    for i in range(10, 100):
        two_list = list(str(i))
        if (two_list[0] != '0' and two_list[1] != '0') \
           and (two_list[0] != two_list[1]):
            twos.append(i)
    return set(twos)

def threes():
    """Return a set of three digit numbers that
    do not repeat or have a zero in them"""
    threes = []
    for i in range(100, 1000):
        three_list = list(str(i))
        if ((three_list[0] != three_list[1]) and (three_list[0] != \
            three_list[2]) and (three_list[1] != three_list[2]))and \
           (three_list[0] != '0' and three_list[1] != '0' \
            and three_list[2] != '0'):
            threes.append(i)
    return set(threes)

def fours():
    """Return a set of four digit numbers that
    do not repeat or have a zero in them"""
    fours = []
    for i in range(1000, 10000):
        four_list = list(str(i))
        if ((four_list[0] != four_list[1]) and (four_list[0] \
            != four_list[2]) and (four_list[0] != four_list[3]) \
            and (four_list[1] != four_list[2]) and \
            (four_list[1] != four_list[3]) and (four_list[2] \
            != four_list[3])) and (four_list[0] != '0' and \
            four_list[1] != '0' and four_list[2] != '0' and \
            four_list[3] != '0'):
            fours.append(i)
    return set(fours)

def is_pandigital(is_pan):
    """Checks if multiplicand, multiplier,
    and the product are pandigital"""
    new = []
    for x in is_pan:
        if x not in new:
            new.append(x)
        else:
            return "False"
            
def pandigital(x, y, z):
    """Multiply the twos and threes together
    and the ones and fours to check for
    pandigitallity"""
    pospan = []
    # check the two * threes
    for i in x:
        for j in y:
            ij = i * j
            i1 = list(str(i))
            j1 = list(str(j))
            product = list(str(ij))
            if len(product) == 4:
                if product[0] == '0' or product[1] == '0' \
                   or product[2] == '0' or product[3] == '0':
                    continue
                else:
                    is_pan = str(i) + str(j) + str(ij)
                    if is_pandigital(is_pan) != "False":
                        print "is_pan =", is_pan
                        pospan.append(ij)
            elif len(product) == 5:
                if product[0] == '0' or product[1] == '0' \
                   or product[2] == '0' or product[3] == '0' \
                   or product[4] == '0':
                    continue
                else:
                    is_pan = str(i) + str(j) + str(ij)
                    if is_pandigital(is_pan) != "False":
                        print "is_pan =", is_pan
                        pospan.append(ij)
            else:
                print "Error Message"
    # check the ones * fours
    for g in range(1, 10):
        for h in z:
            gh = g * h
            g1 = list(str(g))
            h1 = list(str(h))
            product = list(str(gh))
            if len(product) == 4:
                if product[0] == '0' or product[1] == '0' \
                   or product[2] == '0' or product[3] == '0':
                    continue
                else:
                    is_pan = str(g) + str(h) + str(gh)
                    if is_pandigital(is_pan) != "False":
                        print "is_pan =", is_pan
                        pospan.append(gh)
            elif len(product) == 5:
                if product[0] == '0' or product[1] == '0' \
                   or product[2] == '0' or product[3] == '0' \
                   or product[4] == '0':
                    continue
                else:
                    is_pan = str(g) + str(h) + str(gh)
                    if is_pandigital(is_pan) != "False":
                        print "is_pan =", is_pan
                        pospan.append(gh)
    return set(pospan)
    
def main():
    """Main Program"""
    x = twos()
    y = threes()
    z = fours()
    xy = pandigital(x, y, z)
    print xy
    print sum(xy)

if __name__ == '__main__':
    main()

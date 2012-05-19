# Python version 2.7.1
# Platform is win32

from __future__ import division

def find_fractions():
    """Find the curious fractions"""
    num_list = []
    den_list = []
    for n in range(10, 100):
        for d in range(10, 100):
            if d > n:
                x = n / d
                ln = list(str(n))
                ld = list(str(d))
                if (ln[0] == ld[1]) and (ln[0] != '0'):
                    if ld[0] != '0':
                        if (int(ln[1]) / int(ld[0])) == x:
                            print "n/d =", n, d
                            num_list.append(n)
                            den_list.append(d)
                        else:
                            continue
                elif (ln[1] == ld[0]) and (ln[1] != '0'):
                    if ld[1] != '0':
                        if (int(ln[0]) / int(ld[1])) == x:
                            print "n/d =", n, d
                            num_list.append(n)
                            den_list.append(d)
                    else:
                        continue
                else:
                    continue
    return num_list, den_list

def find_product(num_list, den_list):
    """Find the product of these four fractions,
    then divide the denominator by the numerator"""
    num_prod = 1
    den_prod = 1
    for i in num_list:
        num_prod = num_prod * i
    for j in den_list:
        den_prod = den_prod * j
    answer = den_prod / num_prod
    return answer
    
def main():
    """Main Program"""
    y = find_fractions()
    x = find_product(y[0], y[1])
    print "Answer = ", x
        
if __name__ == '__main__':
    main()

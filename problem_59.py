# Python version = 2.7.1
# Platform = win32

import itertools

def main():
    f = open('cipher1.txt', 'r')
    f = f.read()
    #print f
    f.split(',')
    for element in f:
        if element != ',':
            #print ord(element), element
            pass
    L = itertools.permutations('abcdefghijklmnopqrstuvwxyz', 3)
    counter = 0
    for i in L:
        #print "".join(i)
        counter += 1
    print counter


if __name__ == '__main__':
    main()

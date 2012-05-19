# Python version = 2.7.1
# Platform = win32

import math

def count_occ(L):
    """Count occurrences of items in list L
    and return the Answer"""
    Answer = 0
    for i in L:
        x = L.count(i)
        if x > Answer:
            Answer = i
    return Answer

def main():
    """Main Program"""
    L = []
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = math.sqrt((a ** 2) + (b ** 2))
            p = a + b + c
            if p % 1 == 0 and p <= 1000:
                L.append(p)
            else:
                continue
    Answer = count_occ(L)
    print "Answer = ", Answer
        
if __name__ == '__main__':
    main()

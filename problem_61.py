# Python version = 2.7.1
# Platform = win32

def find_triangle():
    """Find all 4 digit triangle numbers"""
    L = []
    for n in range(1, 200):
        p3 = n * (n + 1) / 2
        p3 = str(p3)
        if len(p3) == 4:
            L.append(p3)
    return L

def find_square():
    """Find all 4 digit square numbers"""
    L = []
    for n in range(1, 110):
        p4 = pow(n, 2)
        p4 = str(p4)
        if len(p4) == 4:
            L.append(p4)
    return L

def find_pentagonal():
    """Find all 4 digit pentagonal numbers"""
    L = []
    for n in range(1, 100):
        p5 = n * ((3 * n) - 1) / 2
        p5 = str(p5)
        if len(p5) == 4:
            L.append(p5)
    return L

def find_hexagonal():
    """Find all 4 digit hexagonal numbers"""
    L = []
    for n in range(1, 100):
        p6 = n * ((2 * n) - 1)
        p6 = str(p6)
        if len(p6) == 4:
            L.append(p6)
    return L

def find_heptagonal():
    """Find all 4 digit heptagonal numbers"""
    L = []
    for n in range(1, 100):
        p7 = n * ((5 * n) - 3) / 2
        p7 = str(p7)
        if len(p7) == 4:
            L.append(p7)
    return L

def find_octagonal():
    """Find all 4 digit octagonal numbers"""
    L = []
    for n in range(1, 100):
        p8 = n * ((3 * n) - 2)
        p8 = str(p8)
        if len(p8) == 4:
            L.append(p8)
    return L
    
def main():
    p3 = set(find_triangle())
    p4 = set(find_square())
    p5 = set(find_pentagonal())
    p6 = set(find_hexagonal())
    p7 = set(find_heptagonal())
    p8 = set(find_octagonal())
    for i3 in p3:
        for i8 in p8:
            if i8[2:] == i3[:2]:
                print i8[2:]
                print i3[:2]
                print "\n"
                            
if __name__ == '__main__':
    main()

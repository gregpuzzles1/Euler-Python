# Python version = 2.7.1
# Platform = win32

letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, \
        'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, \
        'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, \
        'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

def get_word_value(xy):
    """Add up the value of the letters in the word xy"""
    counter = 0
    for i in xy:
        val = letters[i]
        counter = counter + val
    return counter

def get_triangle_number():
    """Create list L of triange numbers"""
    L = []
    for n in range(100):
        t = (.5 * n) * (n + 1)
        L.append(t)
    return L

def is_value_triangle_number(c, y):
    """Is the value of the word == to a triangle number?"""
    if c not in y:
        return False
    else:
        return True

def main():
    """Main Program"""
    L1 = []
    y = get_triangle_number()
    f = open('words.txt', "r")
    words = str(f.read())
    x = words.split('","')
    for word in x:
        if word == '"A':
            first = 'A'
            c = get_word_value(first)
            if is_value_triangle_number(c, y) == True:
                L1.append(first)
            else:
                continue
        elif word == 'YOUTH"':
            last = 'YOUTH'
            c = get_word_value(last)
            if is_value_triangle_number(c, y) == True:
                L1.append(last)
            else:
                continue
        elif word != '"A' or word != 'YOUTH"':
            xy = list(word)
            c = get_word_value(xy)
            if is_value_triangle_number(c, y) == True:
                L1.append(c)
            else:
                continue
        else:
            print "Error Message"
    print "Answer = ", len(L1)
            
if __name__ == '__main__':
    main()

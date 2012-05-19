f = open('names.txt', 'rU')
names = []

names = sorted(f.read().replace('"', '').split(','), key=str)

letv = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10, \
        'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19, \
        'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def letter_counter(letter):
    """Letter counter"""
    lc = letv[letter]
    return lc
   
def main():
    """Main program"""
    x = len(names)
    z = 0
    for i in range(0,(x)):
        x2 = 0
        y = 0
        for letter in names[i]:
            x1 = letter_counter(letter)
            x2 = x2 + x1
        y = x2 * (i + 1)
        z = z + y
    print "z = ", z
            
if __name__ == '__main__':
    main()

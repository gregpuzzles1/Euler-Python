# Python version = 2.7.2
# Platform = win32

def main():
    f = open('one-hundred_50.txt', 'rU')
    tally = 0 
    for g in f.readlines():
        gpl = g.replace('\n', '')
        if gpl.isdigit():
            number = int(gpl)
            tally = number + tally
        else:
            print "The varialble gpl contains no digit"
    f.close()
    print "tally = ", tally

if __name__ == '__main__':
    main()

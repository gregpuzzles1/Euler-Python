# Python version = 2.7.1
# Platform = win32

def palindromic(tally):
    """Check if number (tally) is a palindrome"""
    x = str(tally)
    y = x[::-1]
    if x == y:
        return True
    else:
        return False

def isLychrel(n):
    """Check if number (n) is a Lychrel number"""
    counterL = 0
    while counterL < 50:
        reverse = int(str(n)[::-1])
        tally = n + reverse
        if palindromic(tally):
            return False
        else:
            n = tally
        counterL += 1
    return True
   
def main():
    """Main Program"""
    counter = 0
    for n in range(10, 10001):
        if isLychrel(n):
            counter += 1
    print "Answer = ", counter

if __name__ == '__main__':
    main()

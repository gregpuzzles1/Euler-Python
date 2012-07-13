# Python version = 2.7.2
# Platform = win32

from math import factorial

def main():
    """Main Program"""
    n = 100
    Sum = 0
    result = factorial(n)
    string_result = str(result)
    for number in string_result:
        Sum += int(number)
    print "Sum = %d" % Sum        
    
if __name__ == '__main__':
    main()

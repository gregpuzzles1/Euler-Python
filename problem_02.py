# Python version = 2.7.2
# Platform = win32

def fib(n):
    """Determines the sum of the even numbers in the fibonacci sequence
    up to value n"""
    thesum = 0
    a, b = 0, 1
    while a < n:
        if a % 2 == 0:
            thesum = (thesum + (a))
        a, b = b, a + b
    return thesum

def main():
    """The main program - calls the fib function and prints the value
    returned from the function --> x"""
    x = fib(4000000)
    print x
    
if __name__ == '__main__':
    main()

# Python version: 2.7.2
# Platform = win32

def main():
    """Finds the difference between the sum of the
    squares of the first one hundred natural numbers
    and the square of the sum."""
    sum_of_squares = 0
    square_of_sum = 0
    Sum = 0
    for i in range(1, 101):
        square = i ** 2
        sum_of_squares += square
        Sum += i
    square_of_sum = Sum ** 2
    print "sum_of_squares = ", sum_of_squares
    print "square_of_sum = ", square_of_sum
    Difference = square_of_sum - sum_of_squares
    print "Difference = ", Difference

if __name__ == '__main__':
    main()

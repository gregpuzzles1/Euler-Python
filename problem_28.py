def add_diagonal(passed):
    """Calculate sum of individual diagonal"""
    summer = 1
    adder = 0
    tallyer = 0
    for i in range(0, 500):
        if i < 1:
            adder = passed
        else:
            adder = adder + 8
        summer = summer + adder
        tallyer = tallyer + summer
    return tallyer
        
def main():
    """Main program:
    Finds sum of each diagonal
    and adds 1 for the center"""
    lr = add_diagonal(2)
    print "lr = ", lr
    ll = add_diagonal(4)
    print "ll = ", ll
    ul = add_diagonal(6)
    print "ul = ", ul
    ur = add_diagonal(8)
    print "ur = ", ur
    tally = lr + ll + ul + ur + 1
    print "tally = ", tally

if __name__ == '__main__':
    main()

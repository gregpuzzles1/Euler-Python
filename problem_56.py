# Python version = 2.7.1
# Platform = win32

def main():
    """Main Program"""
    answer = 0 
    for a in range(1, 101):
        for b in range(1, 101):
            natural_number = a ** b
            L = list(str(natural_number))
            digital_sum = 0
            for i in L:
                digital_sum = digital_sum + int(i)
            if digital_sum > answer:
                answer = digital_sum
    print "Answer = ", answer

if __name__ == '__main__':
    main()

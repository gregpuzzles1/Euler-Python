# Python version = 2.7.2
# Platform = win32

def main():
    """Main Program"""
    result = 2 ** 1000
    string_result = str(result)

    Sum = 0
    for number in string_result:
        Sum = Sum + int(number)
        
    print Sum

if __name__ == '__main__':
    main()

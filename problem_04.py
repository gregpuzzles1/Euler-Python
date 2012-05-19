# Python version = 2.7.2
# Platform = win32

def findLargest():
    largest = 0
    for i in range (100, 999):
        for r in range(100, 999):
            x = str(i * r)
            y = x[::-1]
            if x == y:
                x = int(x)
                if x > largest:
                    largest = (x)
    return largest

def main():
    print findLargest()
        
if __name__ == '__main__':
    main()

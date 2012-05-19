# Python version = 2.7.1
# Platform = win32
# stop_time =  11.3020665768 (seconds)

import time

d = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", \
     5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

def main():
    """Main Program"""
    start_time = time.clock()
    counter = 1
    while counter < 150000:
        L = []
        for n in range(2, 7):
            result = str(counter * n)
            L.append(result)
        L3 = []
        for number in L:
            L2 = []
            for i, digit in enumerate(number):
                s = int(digit)
                L2.append(d[s])
            L3.append(L2)
        if cmp(sorted(L3[0]), sorted(L3[1])) == 0 and \
           cmp(sorted(L3[0]), sorted(L3[2])) == 0 and \
           cmp(sorted(L3[0]), sorted(L3[3])) == 0 and \
           cmp(sorted(L3[0]), sorted(L3[4])) == 0:
            print "YAHOO = ", counter
        counter += 1
    stop_time = time.clock() - start_time
    print "stop_time = ", stop_time
    
if __name__ == '__main__':
    main()

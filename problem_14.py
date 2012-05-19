largest = 0
for n in range(2, 1000001):
    counter = 1
    number = n
    while n > 1:
        if n%2 == 0:
            n = n/2
            counter += 1
        else:
            n = n*3 + 1
            counter += 1

    if counter > largest:
        largest = counter
        print "largest = ", largest
        print "starting number = ", number





        



# Python version = 2.7.2
# Platform = win32

fjf = open('1000.txt', 'rU')
bcm = fjf.readlines()
hws = ''.join(bcm)
bvc = hws.replace('\n', '')
fjf.close()

largest = 0

for i in range(0, (len(bvc) - 4)):
    fiveDigits = bvc[i:(i + 5)]

    x1 = int(fiveDigits[0:1])
    x2 = int(fiveDigits[1:2])
    x3 = int(fiveDigits[2:3])
    x4 = int(fiveDigits[3:4])
    x5 = int(fiveDigits[4:5])
    
    product = x1 * x2 * x3 * x4 * x5
    
    if product > largest:
        largest = product
        
print "Greatest product is: %s" % largest

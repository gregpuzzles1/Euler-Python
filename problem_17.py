number = {
    1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
    8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
    14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
    18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'fourty',
    50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
    100:'hundred',1000:'thousand'}

tally = 0
for n in range(1,1001):
    if n > 20 and n!=20 and n!=30 and n!=40 and n!=50 and n!=60 and \
       n!=70 and n!=80 and n!=90 and n!=100 and n!=200 and n!=300 \
       and n!=400 and n!=500 and n!=600 and n!=700 and n!=800 and n!=900: 
        if n > 99 and n!=100 and n!=200 and n!=300 and n!=400 and \
           n!=500 and n!=600 and n!=700 and n!=800 and n!=900 and n!=1000:
            x1 = str(n)
            x1a = x1[0:1]
            x1aa = len(number[int(x1a)])
            x2 = x1[1:2]
            x3 = x1[2:]
            x5 = x1[1:3]
            if x2 == '0' and x3 != '0':
                k = 3 + x1aa+len(number[int(x3)])+(len(number[100]))
                #tally = tally + k
                print "n= %s k= %s tally= %s" % (n,k,tally)
                tally = tally + k
                continue
            
            elif x2 != '0' and (x3 != '0'): 
                if x1[1] == '1':
                    k = 3 + x1aa + len(number[int(x5)])+(len(number[100]))
                    #tally = tally + k
                    print "n2= %s k2= %s tally= %s" % (n,k,tally)
                    tally = tally + k
                    continue
                  
                else:
                    x4 = str(x2 + '0')
                    k = 3 + x1aa + len(number[int(x4)])+len(number[int(x3)])+(len(number[100]))
                    #tally = tally + k
                    print "nn3= %s kk3= %s tally= %s" % (n,k,tally)
                    tally = tally + k
                    continue
                   
            elif x3 == '0':
                k = 3 + x1aa + len(number[int(x5)])+(len(number[100]))
                #tally = tally + k
                print "nnn4= %s kkk4= %s tally= %s" % (n,k,tally)
                tally = tally + k
                continue
              
            else:
                print "You may have an error in your program"
        elif n == 1000:
            k = (len(number[1]))+(len(number[1000]))
            #tally = tally + k
            print "nnnn5= %s kkkk5= %s tally= %s" % (n,k,tally)
            tally = tally + k
            continue
          
        else:
            x1 = str(n)
            x2 = x1[0:1]
            x3 = x1[1:]
            x4 = str(x2 + '0')
            k = len(number[int(x4)])+(len(number[int(x3)]))
            #tally = tally + k
            print "nnnnn6= %s kkkkk6= %s tally= %s" % (n,k,tally)
            tally = tally + k
            continue
          
    elif n==100 or n==200 or n==300 or n==400 or n==500 or n==600 or n==700 or n==800 or n==900 and n!=1000:
        x5 = str(n)
        x6 = x5[0:1]
        k = (len(number[int(x6)]))+(len(number[100]))
        #tally = tally + k
        print "nnnnnn7= %s kkkkkk7= %s tally= %s" % (n,k,tally)
        tally = tally + k
        continue
       

    else:
        k = len(number[n])
        #tally = tally + k
        print "nnnnnnn8= %s kkkkkkk8= %s tally= %s" % (n,k,tally)
        tally = tally + k
        continue
      
    #tally = tally + k
print "Final Tally = %s" % tally

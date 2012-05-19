f = open('one-hundred_50.txt', 'rU')
tally = 0 
for g in f.readlines():
    gpl = g.replace('\n', '')
    if gpl.isdigit():
        number = int(gpl)
        print "number= ", number
        tally = number + tally
    else:
        print "The varialble gpl contains no digit"
f.close()
print "tally= ", tally



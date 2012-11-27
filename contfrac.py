from math import sqrt, log, floor

def contfrac(a): ### continued fraction expansion
    terms=[]
    count=0
    b=1
    while ((b != 0) and (count < 24)): ### 24 times, emprical accuracy
    ### limit
        terms.append(floor(a/(b+0.0)))
        a,b = b, a % b
        count = count + 1
        return terms


def ra(x): ### 'rational approximation', or convergent
    numerators=[0,1]
    denominators=[1,0]
    expansion=contfrac(x) ### call the contfrac function
    for num in expansion: ### [-1] and [-2] index 'previous'
    ### and 'previous-previous'
        numerators.append((num*numerators[-1])+numerators[-2])
        denominators.append((num*denominators[-1])+denominators[-2])
    for index in range(len(numerators)):
        print "%i/%i" % (numerators[index], denominators[index])
        print

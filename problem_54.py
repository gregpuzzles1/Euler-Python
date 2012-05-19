# Python version = 2.7.1
# Platform = win32

from collections import Counter

d = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, \
     '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, \
     'K': 13, 'A': 14, 'One Pair': 29, 'Two Pairs': 59, \
     'Three of a Kind': 74, 'Straight': 89, 'Flush': 104, \
     'Full House': 119, 'Four of a Kind': 134,
     'Straight Flush': 149, 'Royal Flush': 164}

def high_card(dL):
    """Is the hand High Card?"""
    holder = 0
    if len(dL) == 5:
        return True
    else:
        return False

def one_pair(dL):
    """Is the hand One Pair?"""
    if len(dL) == 4:
        for k, v in dL.iteritems():
            if v == 2:
                return True
            else:
                continue
    else:
        return False

def two_pairs(dL):
    """Is the hand Two Pairs?"""
    counter = 0
    k1 = 0
    if len(dL) == 3:
        for k, v in dL.iteritems():
            if v == 2:
                if k > k1:
                    k1 = k
                counter += 1
                if counter == 2:
                    return True
            else:
                continue
    else:
        return False
    
def three_of_a_kind(dL):
    """Is the hand Three of a Kind?"""
    if len(dL) == 3:
        for k, v in dL.iteritems():
            if v == 3:
                return True
            else:
                continue
    else:
        return False

def straight(L):
    """Is the hand a Straight?"""
    L = sorted(L)
    if (L[0] + 1) == L[1] and (L[0] + 2) == \
       L[2] and (L[0] + 3) == L[3] and \
       (L[0] + 4) == L[4]:
        return True
    else:
        return False
    
def flush(L1):
    """Is the hand a Flush"""
    if len(Counter(L1)) == 1:
        return True
    else:
        return False

def full_house(dL):
    """Is the hand a Full House?"""
    if len(dL) == 2:
        for k, v in dL.iteritems():
            if v == 3:
                return True
            else:
                continue
    else:
        return False

def four_of_a_kind(dL):
    """Is the hand Four of a Kind?"""
    if len(dL) == 2:
        for k, v in dL.iteritems():
            if v == 4:
                return True
            else:
                continue
    else:
        return False

def straight_flush(L, L1):
    """Is the hand a Straight Flush?"""
    L = sorted(L)
    if len(Counter(L1)) == 1 and \
       ((L[0] + 1) == L[1] and (L[0] + 2) == \
       L[2] and (L[0] + 3) == L[3] and \
       (L[0] + 4) == L[4]):
        return True
    else:
        return False

def royal_flush(L, L1):
    """Is the hand a Royal Flush?"""
    if len(Counter(L1)) == 1 and sum(L) == 60:
        return True
    else:
        return False
    
def examine_cards(cards):
    """Examine Cards"""
    L, L1 = [], []
    dL = {}
    for i in range(0, 9, 2):
        x1 = d[cards[i]]
        L.append(x1)
    for i in range(1, 10, 2):
        x1 = cards[i]
        L1.append(x1)
    for i in L:
        dL[i] = L.count(i)
    if royal_flush(L, L1):
        return d['Royal Flush']
    elif straight_flush(L, L1):
        return d['Straight Flush']
    elif four_of_a_kind(dL):
        c1 = 0
        for k, v in dL.iteritems():
            if v == 4:
                c1 = k
        return d['Four of a Kind'] + c1
    elif full_house(dL):
        c2 = 0
        for k, v in dL.iteritems():
            if v == 3:
                c2 = k
        return d['Full House'] + c2
    elif flush(L1):
        c3 = 0
        for k, v in dL.iteritems():
            if k > c3:
                c3 = k
        return d['Flush'] + c3
    elif straight(L):
        c4 = 0
        for k, v in dL.iteritems():
            if k > c4:
                c4 = k
        return d['Straight'] + c4
    elif three_of_a_kind(dL):
        c5 = 0
        for k, v in dL.iteritems():
            if v == 3:
                c5 = k
        return d['Three of a Kind'] + c5
    elif two_pairs(dL):
        k1 = 0
        for k, v in dL.iteritems():
            if v == 2:
                if k > k1:
                    k1 = k
        return d['Two Pairs'] + k1
    elif one_pair(dL):
        c6 = 0
        for k, v in dL.iteritems():
            if v == 2:
                c6 = k
        return d['One Pair'] + c6 
    elif high_card(dL):
        count1 = 0
        for k, v in dL.iteritems():
            if k > count1:
                count1 = k
        return count1
    else:
        print "***Error Message***"
    
def main():
    """Main Program"""
    player1 = 0
    f = open('poker.txt', 'r')
    for line in f:
        x = line.split(' ')
        y = ''.join(x)
        player_one = y[0:10]
        player_two = y[10:20]
        j = examine_cards(player_one)
        t = examine_cards(player_two)
        if j == t:
            print "player_one = ", player_one
            print "player_two = ", player_two
            print "EQUAL"
        elif j < t:
            continue
        elif j > t:
            player1 += 1
        else:
            pass
    f.close()
    print "Answer = ", player1
    
if __name__ == '__main__':
    main()

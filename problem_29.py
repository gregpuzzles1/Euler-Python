def get_terms():
    """Find the terms and put them in a list L,
    return the set of list L"""
    L = []
    for a in range(2, 101):
        for b in range(2, 101):
            term = (a ** b)
            L.append(term)
    return set(L)

def main():
    """Main program"""
    x = get_terms()
    print "Number of Terms = ", len(x)
    
if __name__ == '__main__':
    main()

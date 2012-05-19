def main():
    """Help from: http://blog.dreamshire.com/2009/03/31/project-euler-problem-31-solution/"""
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1]+[0]*target
    for coin in coins:
        for i in range(coin, target+1):
            ways[i] += ways[i-coin]
    print "Ways = ", ways[target]
    
if __name__ == '__main__':
    main()
    

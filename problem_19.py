def find_days(month, yr):
    if (month == 1) or (month == 3) or (month == 5) or (month == 7) \
       or (month == 8) or (month == 10) or (month == 12):
        d = 31
        return d
    elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
        d = 30
        return d
    elif (month == 2):
        if yr%4 == 0:
            if yr%100 == 0:
                if yr%400 == 0:
                    d = 29
                    return d
                else:
                    d = 28
                    return d
            d = 29
            return d
        else:
            d = 28
            return d
        
    else:
        print "There has been an error"

def main():
    for yr in range(1900,2001):
    # Year
        print "\n&&&&&&&&&&&&&&&&&&&&&&&year = ", yr
        
        for month in range(1,13):
        # Month
            print "\nmonth= ", month
            y = find_days(month, yr)
            print "MONTH_DAYS = ", y
            for days in range(1,(y+1)):
            # Days
                #print "day= ", days,
                pass
                         

if __name__ == '__main__':
    main()
        

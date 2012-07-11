# Python version = 2.7.2
# Platform = win32

def find_days(month, yr):
    """Finds the number of days the month has"""
    if (month == 1) or (month == 3) or (month == 5) or (month == 7) \
       or (month == 8) or (month == 10) or (month == 12):
        d = 31
        return d
    elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
        d = 30
        return d
    elif (month == 2):
        if yr % 4 == 0:
            if yr % 100 == 0:
                if yr % 400 == 0:
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
        
L = {1:'Sun', 2:'Mon', 3:'Tue', 4:'Wed', 5:'Thurs', 6:'Fri', 7:'Sat'}

def main():
    """Main Program"""
    counter = 1 # Start at Monday, 1st, 1900
    tally = 0
    for yr in range(1900, 2001):
    # Year  
        print "\nYear = ", yr
        
        for month in range(1, 13):
        # Month
            y = find_days(month, yr)
            
            for month_days in range(1, (y + 1)):
            # Number of month days
                counter = counter + 1        
                if (month_days == 1) and L[counter] == "Sun":
                    print "month_days = %s L[counter]= %s " \
                          % (month_days, L[counter])
                    tally = tally + 1
                if counter >= 7: # Days of the week
                    counter = 0
    print "\nTally = ", (tally - 2)
    # subtract 2 for the year 1900                

if __name__ == '__main__':
    main()

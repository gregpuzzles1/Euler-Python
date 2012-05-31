# Project Euler - Problem 14
import math
print "\nProject Euler - Problem 14"
print "For the sequence: \n"
print "n -> n/2 (if n is even)"
print "n -> 3n+1 (if n is odd)\n"
print "Find the longest chain that ends in '1'"
 
start = 10**6
num = (start/2)
ans = 0
maxcnt=0
while num < start:
    x = num
    cnt = 1
    while x != 1:
        if x & 1: x = 3*x + 1 # odd
        else: x >>= 1 # even
        cnt += 1
        if cnt > maxcnt:
            ans = num
            maxcnt = cnt
    num += 1
print ans

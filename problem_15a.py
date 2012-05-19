# Euler 15
# http://projecteuler.net/index.php?section=problems&id=15
# Starting in the top left corner of a 2x2 grid, there
# are 6 routes (without backtracking) to the bottom right
# corner. How many routes are their in a 20x20 grid?
import time
start = time.time()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

rows, cols = 20, 20
print factorial(rows+cols) / (factorial(rows) * factorial(cols))

print "Elapsed Time:", (time.time() - start) * 1000, "millisecs"
a=raw_input('Press return to continue')

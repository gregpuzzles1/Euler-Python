def divides(n):
    return len(sorted(set(sum( ([x,n/x] for x in range(1, int(n**0.5+0.5) + 1) if not n%x), [] ))))

tri_num = 0
for i in xrange(0, 200000):
    tri_num = tri_num + i
    if divides(tri_num) >= 500:
        print "tri_num = %s" % tri_num
        break


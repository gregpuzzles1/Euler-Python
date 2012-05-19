sumu = 1
for i in range(1, 101):
    sumu = sumu * i
x = str(sumu)
temp = 0
for i in x:
    temp = temp + int(i)
print temp

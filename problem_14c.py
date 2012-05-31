def is_even(n):
    return n % 2 == 0

def collatz_length(n):
    length = 0
    while n > 1:
        length += 1
        if is_even(n):
            n /= 2
        else:
            n = 3 * n + 1
    return length

max_n = 0
max_len = 0

for n in range(1, 1000000):
    len = collatz_length(n)
    if len > max_len:
        max_len = len
        max_n = n

print max_n


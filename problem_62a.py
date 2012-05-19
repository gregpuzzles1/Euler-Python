import collections, itertools
def problem62():
    # In this dictionary, keys are sorted strings of digits and values are
    # lists of numbers whose cubes contain those digits in some order.
    cubes = collections.defaultdict(list)
    for i in itertools.count(1):
        c = cubes[''.join(sorted(str(i ** 3)))]
        c.append(i)
        if len(c) == 5:
            return c

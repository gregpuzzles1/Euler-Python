import math

def CF_of_sqrt(n):
    """ Compute the continued fraction representation of the
        square root of N.

        The first element in the returned array is the whole
        part of the fraction. The others are the denominators
        up to (and not including) the point where it starts
        repeating.

        Uses the algorithm explained here:
        http://www.mcs.surrey.ac.uk/Personal/R.Knott/Fibonacci/cfINTRO.html
        In the section named: "Methods of finding continued
        fractions for square roots"
    """
    if is_square(n):
        return [int(math.sqrt(n))]

    ans = []

    step1_num = 0
    step1_denom = 1

    while True:
        nextn = int((math.floor(math.sqrt(n)) + step1_num) / step1_denom)
        ans.append(int(nextn))

        step2_num = step1_denom
        step2_denom = step1_num - step1_denom * nextn

        step3_denom = (n - step2_denom ** 2) / step2_num
        step3_num = -step2_denom

        if step3_denom == 1:
            ans.append(ans[0] * 2)
            break

        step1_num, step1_denom = step3_num, step3_denom

    return ans

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def pells_solved(x, y, D):
    if (x ** 2) - (D * (y ** 2)) == 1:
        return True
    else:
        return False

def find_num_denom(convergents, D):
    a = convergents[:1]
    period = convergents[1:]
    switch = 0
    while switch == 0:
        period[0:1]
        elif len(period) == 1:
            numerator = period[i] * a
            denominator = period[i]
            if pells_solved(numerator, denominator, D)
                switch = 1
        elif len(period) > 1:

def main():
    for D in range(2, 1001):
        convergents = CF_of_sqrt(D)
        if len(convergents) == 1:
            continue
        else:
            find_num_denom(convergents, D)

if __name__ == '__main__':
    main()

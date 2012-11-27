import fractions
from fractions import Fraction

def cf3(terms, iterations):
     
    answer = 0
     
    for n in range(iterations, 0, -1):
        answer = Fraction(1, terms[n] + answer)
     
    answer += Fraction(terms[0], 1)
     
    return answer

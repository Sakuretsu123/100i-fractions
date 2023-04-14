#!python3

# Create a function that receives 2 parameters:
# numerator (integer) and denominator (integer)
# return a tuple of 2 integers (numerator, denominator) for 
# the fraction in lowest terms

from typing import final


def lowestTerms(numerator,denominator):
    myList = [numerator, denominator]
    multiplicators = []
    final= []
    x = max(myList)
    for i in range(1, x): 
        num = numerator%i
        den = denominator%i
        if num == 0 and den == 0: 
            multiplicators.append(i)
    
    n = max(multiplicators)
    num = num//n 
    den = den//n 
    final.append(num)
    final.append(den)

    return final
        
    







def main():
    assert lowestTerms(2,4) == (1,2)
    assert lowestTerms(32,40) == (4,5)
    assert lowestTerms(29,87) == (1,3)
    assert lowestTerms(250,400) == (5,8)

if __name__ == "__main__":
    main()

    
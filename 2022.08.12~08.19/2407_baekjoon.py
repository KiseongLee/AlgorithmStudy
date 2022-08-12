from fractions import Fraction
n, m = map(int, input().split())

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    
    return fact

def combinations(n,m):
    # return Fraction(fact(n), (fact(n-m)*fact(m)))
    return fact(n)//(fact(n-m)*fact(m))


print(combinations(n,m))



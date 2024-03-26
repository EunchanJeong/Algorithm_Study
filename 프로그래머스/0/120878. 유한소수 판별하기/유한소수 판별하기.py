import math

def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    return factors

def solution(a, b):
    k = math.gcd(a, b)
    
    b = b//k
    p = list(set(prime_factors(b)))
    
    if b == 1:
        return 1

    if len(p) == 2:
        if p[0] == 2 and p[1] == 5:
            return 1
    elif len(p) == 1:
        if p[0] == 2 or p[0] == 5:
            return 1    
    return 2
import math

def solution(numer1, denom1, numer2, denom2):
    if denom1 <= denom2:
        tmp = denom1
        denom1 = denom2
        denom2 = tmp
        
        tmp = numer1
        numer1 = numer2
        numer2 = tmp
    

    if denom1 % denom2 == 0:
        count = 1
        while denom2 != denom1:
            denom2 *= count
            numer2 *= count
            
            count += 1
        denom = denom1
    else:
        numer1 *= denom2
        numer2 *= denom1
        
        denom = denom1*denom2
    
    numer = numer1+numer2

    g = math.gcd(numer, denom)
    numer //= g
    denom //= g
    
    answer = [numer, denom]
    return answer
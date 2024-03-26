def factorial(k):
    x = 1
    
    for i in range(k, 1, -1):
        x *= i
        
    return x

def solution(balls, share):
        
    answer = factorial(balls) // (factorial(balls-share) * factorial(share))
    return answer
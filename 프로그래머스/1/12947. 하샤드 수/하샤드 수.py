def solution(x):
    num = 0
    for n in str(x):
        num += int(n)
    
    answer = True
    
    if x % num != 0:
        answer = False
        
    return answer
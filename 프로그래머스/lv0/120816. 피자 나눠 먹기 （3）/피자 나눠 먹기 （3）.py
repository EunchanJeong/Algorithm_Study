def solution(slice, n):
    answer = 0
    
    for i in range(1, n+1):
        if i * slice >= n:
            answer = i
            break
            
    return answer
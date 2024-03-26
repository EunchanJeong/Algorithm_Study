def solution(numbers, k):
    answer = 0
    idx = 0
    
    for _ in range(k):
        answer = numbers[idx]
        idx += 2
        
        if idx >= len(numbers):
            idx -= len(numbers)
    return answer
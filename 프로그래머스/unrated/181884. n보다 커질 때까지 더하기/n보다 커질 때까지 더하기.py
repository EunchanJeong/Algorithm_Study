def solution(numbers, n):
    answer = 0
    
    for num in numbers:
        if answer <= n:
            answer += num
        else:
            break
    return answer
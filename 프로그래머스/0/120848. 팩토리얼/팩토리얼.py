def solution(n):
    answer = 0
    for i in range(1, 11):
        f = 1
        
        for j in range(i, 1, -1):
            f *= j

        if n >= f:
            answer = i
        else:
            break
    return answer
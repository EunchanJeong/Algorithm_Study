def solution(n):
    answer = 0
    for i in range(1, n+1):
        if i*7 >= n:
            answer = i
            break

    return answer
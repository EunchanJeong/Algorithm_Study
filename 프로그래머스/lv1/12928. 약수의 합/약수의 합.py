def solution(n):
    answer = sum([num for num in range(1, n+1) if n%num==0])
    return answer
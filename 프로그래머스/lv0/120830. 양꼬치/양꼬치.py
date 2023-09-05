def solution(n, k):
    ten_count = n//10
    answer = (n*12000) + ((k-ten_count)*2000)
    return answer
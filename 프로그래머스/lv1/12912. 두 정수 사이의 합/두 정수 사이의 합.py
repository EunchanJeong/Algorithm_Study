def solution(a, b):
    if a > b:
        tmp = a
        a = b
        b = tmp
        
    answer = sum([x for x in range(a, b+1)])
    return answer
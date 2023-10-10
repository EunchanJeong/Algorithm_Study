def solution(n):
    answer = int(n**(1/2))**2
    if n != answer:
        return -1
    else:
        return (int(n**(1/2))+1)**2
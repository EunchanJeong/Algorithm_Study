def solution(n):
    n = str(n)
    
    n = [x for x in n]
    n.sort(reverse=True)
    
    answer = int("".join(n))
    
    return answer
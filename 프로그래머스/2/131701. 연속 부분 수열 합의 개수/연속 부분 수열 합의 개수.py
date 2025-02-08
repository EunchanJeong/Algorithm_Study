def solution(elements):
    n = len(elements)
    elements = elements * 2
    
    S = set()
    
    for l in range(1, n+1):
        for start in range(n):
            sum_num = sum(elements[start:start+l])
            
            S.add(sum_num)
    
    return len(S)
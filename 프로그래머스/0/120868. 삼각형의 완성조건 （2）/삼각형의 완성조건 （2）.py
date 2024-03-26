def solution(sides):
    sides.sort()
    m = max(sides)
    
    answer = 0
    
    for i in range(1, m+1):
        if sides[0] + i > m:
            answer += 1
    
    k = m+1
    
    while k < sum(sides):
        answer += 1
        k += 1

    return answer
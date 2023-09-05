def solution(s1, s2):
    answer = 0
    
    sum = len(s1) + len(s2)
    tmp =  len(list(set(s1+s2)))
    answer = (sum-tmp)
    return answer
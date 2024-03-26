def solution(num_list, n):
    
    tmp = []
    answer = []
    
    for num in num_list:
        tmp.append(num)
        
        if len(tmp) == n:
            answer.append(tmp)
            tmp = []
    
    return answer
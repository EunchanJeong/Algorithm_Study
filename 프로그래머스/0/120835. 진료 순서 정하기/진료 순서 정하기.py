def solution(emergency):
    
    tmp = emergency.copy()
    tmp.sort(reverse=True)
    
    answer = []
    
    for i in emergency:
        answer.append(tmp.index(i)+1)
    return answer
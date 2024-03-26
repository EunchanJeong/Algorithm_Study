def solution(my_string):
    
    tmp = []
    
    for s in my_string:
        if s not in tmp:
            tmp.append(s)
    answer = ''.join(tmp)
    return answer
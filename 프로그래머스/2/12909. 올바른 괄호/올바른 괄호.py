def solution(s):
    answer = True
    
    a = []
    
    for i in s:
        if i == '(':
            a.append(i)
        else:
            if len(a) != 0:
                if a.pop() != '(':
                    return False
            else:
                return False
                    
    
    if len(a) == 0:
        return True
    else:
        return False
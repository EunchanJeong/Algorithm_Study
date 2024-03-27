def solution(babbling):
    a = ["aya", "ye", "woo", "ma"]
    
    for idx, b in enumerate(babbling):
        for i in a:
            babbling[idx] = babbling[idx].replace(i, '1')
            
    answer = 0
    
    for i in babbling:
        if i.isdigit():
            answer += 1
    return answer
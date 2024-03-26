def solution(spell, dic):
    answer = 0
    
    for word in dic:
        count = 0
        for s in spell:
            if word.count(s) == 1:
                count += 1
        
        if count == len(spell):
            answer += 1
        
    if answer == 0:
        return 2
    else:
        return 1
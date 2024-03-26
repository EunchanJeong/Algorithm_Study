def solution(s):
    tmp = list(set(list(s)))
    tmp.sort()
    
    letters = {}
    for i in tmp:
        letters[i] = 0
    
    for i in s:
        letters[i] += 1
    
    answer = ''
    
    for key, value in letters.items():
        if value == 1:
            answer += key
    
    if answer == '':
        return ''
    return answer
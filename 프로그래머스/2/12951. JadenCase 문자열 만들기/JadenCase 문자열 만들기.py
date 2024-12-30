def solution(s):
    
    tmp = ''
    words = []
    for i in range(len(s)):
        if s[i] == ' ':
            words.append(tmp)
            tmp = ''
            words.append(s[i])
        else:
            tmp += s[i]
    
    if tmp != ' ':
        words.append(tmp)
    for i in range(len(words)):
        if words[i] == ' ':
            continue
        tmp = list(words[i])
        
        for j in range(len(tmp)):
            if j == 0:
                tmp[j] = tmp[j].upper()
            else:
                tmp[j] = tmp[j].lower()
        
        words[i] = ''.join(tmp)
                
    answer = ''.join(words)
    return answer
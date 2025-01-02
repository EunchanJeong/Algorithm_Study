def solution(s):
    answer = []
    answer.append(0)
    answer.append(0)
    
    while s != '1':
        answer[0] += 1
        answer[1] += s.count('0')
        
        x = ''
        for i in s:
            if i == '1':
                x += i
        
        s = format(len(x), 'b')
        
    return answer
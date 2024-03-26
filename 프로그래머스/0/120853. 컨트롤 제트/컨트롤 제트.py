def solution(s):
    s = s.split()
    answer = 0
    
    for idx, value in enumerate(s):
        if value == 'Z' and idx != 0:
            answer -= int(s[idx-1])
        else:
            answer += int(value)

    return answer
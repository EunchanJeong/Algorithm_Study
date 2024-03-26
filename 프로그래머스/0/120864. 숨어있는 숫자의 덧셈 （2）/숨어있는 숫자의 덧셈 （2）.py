def solution(my_string):
    answer = 0
    num = []
    t = 0
    for s in my_string:
        if s.isdigit():
            if s != '0':
                num.append(s)
            else:
                if len(num) != 0:
                    num.append(s)
            t = 1
        else:
            if len(num) != 0:
                answer += int(''.join(num))
                num = []
    if len(num):
        answer += int(''.join(num))
    if t == 0:
        return 0
    return answer
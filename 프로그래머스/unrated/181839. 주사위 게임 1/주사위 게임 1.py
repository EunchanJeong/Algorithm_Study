def solution(a, b):
    if a%2!=0 and b%2!=0:
        return a**2 + b**2
    else:
        if a%2 != 0 or b%2 != 0:
            return  2 * (a+b)
        else:
            answer = a-b
            
            if answer < 0:
                answer = -(answer)
            return answer
    return answer
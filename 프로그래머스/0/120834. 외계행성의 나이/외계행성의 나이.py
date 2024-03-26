def solution(age):
    
    age = str(age)
    
    answer = ''
    
    for i in age:
        answer += chr(97+int(i))
    return answer
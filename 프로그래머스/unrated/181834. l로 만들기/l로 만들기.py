def solution(myString):
    
    answer = ''.join([x if x > 'l' else 'l' for x in myString])
    return answer
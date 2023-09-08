def solution(array, n):
    answer = 0
    
    while True:
        if n in array:
            array.pop(array.index(n))
            answer += 1
        else:
            break
    return answer
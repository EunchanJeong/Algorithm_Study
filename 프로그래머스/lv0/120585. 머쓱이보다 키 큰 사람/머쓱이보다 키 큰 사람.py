def solution(array, height):
    
    array.append(height)
    array.sort()
    
    idx = array.index(height)
    answer = 0
    
    for i in range(idx, len(array)):
        if array[i] > height:
            answer += 1
    return answer    
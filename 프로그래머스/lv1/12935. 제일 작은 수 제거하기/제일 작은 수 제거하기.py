def solution(arr):
    
    answer = [-1]
    
    if len(arr) != 1:
        arr.pop(arr.index(min(arr)))
        answer = arr
    
    return answer
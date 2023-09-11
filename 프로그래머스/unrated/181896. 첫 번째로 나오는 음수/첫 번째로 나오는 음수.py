def solution(num_list):
    answer = 0
    
    for i, num in enumerate(num_list):
        if num < 0:
            return i
            break
    return -1
def solution(array):
    num_list = [0] * (max(array)+1)
    
    for n in array:
        num_list[n] += 1
    
    max_count = num_list.index(max(num_list))
    
    if len(array) > 1:
        m1 = num_list.pop(num_list.index(max(num_list)))
        m2 = num_list.pop(num_list.index(max(num_list)))
        
        if m1 == m2:
            return -1
    return max_count
def solution(sizes):
    for size in sizes:
        if size[0] < size[1]:
            tmp = size[0]
            size[0] = size[1]
            size[1] = tmp
    r_max = 0
    c_max = 0
    
    for size in sizes:
        if r_max < size[0]:
            r_max = size[0]
        if c_max< size[1]:
            c_max = size[1]
            
    return r_max * c_max
def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    
    m1 = abs((y2-y1)/(x2-x1))
    m2 = abs((y4-y3)/(x4-x3))
    if m1 == m2:
        return 1
    
    m3 = abs((y3-y1)/(x3-x1))
    m4 = abs((y4-y2)/(x4-x2))
    if m3 == m4:
        return 1
    
    m5 = abs((y4-y1)/(x4-x1))
    m6 = abs((y3-y2)/(x3-x2))
    if m5 == m6:
        return 1
    
    return 0
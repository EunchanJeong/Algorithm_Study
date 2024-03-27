def solution(lines):
    line1 = set(x for x in range(lines[0][0],lines[0][1]))
    line2 = set(x for x in range(lines[1][0],lines[1][1]))
    line3 = set(x for x in range(lines[2][0],lines[2][1]))
    
    d = len((line1 & line2) | (line2 & line3) | (line3 & line1))
    
    return d

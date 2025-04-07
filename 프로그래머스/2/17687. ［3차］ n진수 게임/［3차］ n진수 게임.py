def solution(n, t, m, p):
    number = []
    cmp = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
    count = 0
    
    while len(number) <= (t*m):
        tmp = []
        if (count//n >= 1):
            tmp_num = count
            while tmp_num//n != 0:
                tmp.insert(0, tmp_num%n)
                tmp_num = tmp_num//n
            tmp.insert(0, tmp_num)
            number += tmp
            count += 1
        else:
            number.append(count)
            count += 1
    
    mid = []
    for i in range(p-1, m*t, m):
        mid.append(str(number[i]))
        
    for i in range(len(mid)):
        for key, value in cmp.items():
            mid[i] = mid[i].replace(key, value)
    
    return ''.join(mid)
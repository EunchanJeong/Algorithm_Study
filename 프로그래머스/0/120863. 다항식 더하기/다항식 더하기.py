def solution(polynomial):
    x = []
    n = []
    
    polynomial = polynomial.split(' + ')
    
    for i in polynomial:
        if 'x' in i:
            x.append(i)
        else:
            n.append(int(i))
            
    answer = ''
    
    x_n = 0
    for i in x:
        if len(i) == 1:
            x_n += 1
        else:
            x_n += int(i[:-1])
        
    if x_n == 0:
        if sum(n) != 0:
            answer = str(sum(n))
        else:
            answer = '0'
    else:
        xx = ''
        if x_n == 1:
            xx = 'x'
        else:
            xx = str(x_n) + 'x'
        if sum(n) != 0:
            answer = xx + ' + ' + str(sum(n))
        else:
            answer = xx
        
    return answer
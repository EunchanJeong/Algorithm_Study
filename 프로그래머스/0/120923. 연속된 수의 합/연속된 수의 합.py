def solution(num, total):
    n = [x for x in range(1, 1000)]
    nn = [x for x in range(-1000, 1)]
    for i in range(len(n)-3):
        if sum(n[i:i+num]) == total:
            return n[i:i+num]
    
    n = nn + n
    for i in range(len(n)-3):
        if sum(n[i:i+num]) == total:
            return n[i:i+num]
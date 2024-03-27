def distance(a, b):
    return abs(a-b)
def solution(numlist, n):
    numlist.sort(key=lambda x: (distance(x, n), -x))
    
    return numlist
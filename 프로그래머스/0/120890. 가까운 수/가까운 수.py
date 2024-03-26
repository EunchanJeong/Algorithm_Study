def solution(array, n):
    tmp = []
    array.sort()
    for i in array:
        tmp.append(abs(n-i))
        
    answer = array[tmp.index(min(tmp))]
    return answer
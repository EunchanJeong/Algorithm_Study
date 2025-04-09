from collections import deque

def solution(msg):
    answer = []
    dictionary = {}
    for i in range(26):
        dictionary[chr(ord('A') + i)] = i+1
        
    q = deque(msg)
    
    while q:
        tmp = q.popleft()
        
        while q and tmp + q[0] in dictionary:
            tmp += q.popleft()
        
        answer.append(dictionary[tmp])
        
        if q:
            dictionary[tmp + q[0]] = len(dictionary) + 1
            
            
    return answer
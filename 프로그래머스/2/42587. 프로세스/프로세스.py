from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    
    while q:
        max_p = max(q)
        p = q.popleft()
        location -= 1
        
        if p != max_p:
            q.append(p)
            
            if location < 0:
                location = len(q) - 1
        elif p == max_p:
            answer += 1
            if location < 0:
                break
        
    return answer
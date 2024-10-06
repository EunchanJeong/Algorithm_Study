from collections import deque

def solution(n, computers):
    def bfs(i):
        q = deque()
        q.append(i)
        
        while q:
            a = q.popleft()
            visited[a] = 1
            for b in range(n):
                if computers[a][b] and not visited[b]:
                    q.append(b)
    answer = 0
    visited = [0 for i in range(len(computers))]
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
            
    return answer
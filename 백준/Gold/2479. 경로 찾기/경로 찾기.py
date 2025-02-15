from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

codes = [''] + [input().strip() for _ in range(N)]

start, end = map(int, input().split())

visited = [0] * (N+1)

def bfs(s, e):
    visited[s] = 1
    
    q = deque()
    q.append((s, str(s)))
    
    while q:
        num, code = q.popleft()
        
        if num == e:
            return code
        
        for i in range(1, N+1):
            count = 0
            
            if visited[i] == 1:
                continue
            
            for j in range(K):
                if codes[num][j] != codes[i][j]:
                    count += 1
                if count > 1:
                    break
                
            if count == 1:
                visited[i] = 1
                q.append((i, code + ' ' + str(i)))
    
    return -1

print(bfs(start, end))
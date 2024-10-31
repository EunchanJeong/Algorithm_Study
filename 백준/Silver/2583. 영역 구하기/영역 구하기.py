from collections import deque

M, N, K = map(int, input().split())

graph = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[M-j-1][i] = 1
    
result = []
def bfs(x, y):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    q = deque()
    
    q.append((x, y))
    graph[y][x] = 1
    
    size = 1
    while q:
        x, y = q.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if (0 <= nx < N) and (0 <= ny < M) and graph[ny][nx] == 0:
                q.append((nx, ny))
                graph[ny][nx] = 1
                
                size += 1
                
    result.append(size)
        
for i in range(N):
    for j in range(M):
        if graph[j][i] == 0:
            bfs(i, j)

result.sort()
print(len(result))
for r in result:
    print(r, end=' ')
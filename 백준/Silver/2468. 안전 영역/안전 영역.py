from collections import deque

N = int(input())
graph = []
max_num = 0

for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    
    for r in row:
        if r > max_num:
            max_num = r

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y, num):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if graph[nx][ny] > num:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


answer = []

for i in range(max_num):
    count = 0
    visited = [[0]*N for _ in range(N)]
    
    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i)
                count += 1
    answer.append(count)
    
print(max(answer))
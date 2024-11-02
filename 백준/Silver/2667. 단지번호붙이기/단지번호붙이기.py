from collections import deque

N = int(input())

graph = []
for _ in range(N):
    tmp = [int(n) for n in list(input())]
    graph.append(tmp)
    

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
counts = []
def bfs(start):
    q = deque()
    
    graph[start[1]][start[0]] = 0
    count = 1
    q.append(start)
 
    while q:
        x, y = q.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if (nx >= 0 and nx < N) and (ny >= 0 and ny < N) and graph[ny][nx] == 1:
                q.append((nx, ny))
                graph[ny][nx] = 0
                count += 1
    counts.append(count)

for i in range(N):
    for j in range(N):
        if graph[j][i] == 1:
            start = (i, j)
            bfs(start)
counts.sort()

print(len(counts))
for c in counts:
    print(c)
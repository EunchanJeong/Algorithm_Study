from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append([int(x) for x in list(input())])

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    
    while q:
        x, y, z = q.popleft()
        
        if x == N-1 and y == M-1:
            return visited[x][y][z]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))
                    
                elif graph[nx][ny] == 1 and z == 0:
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
                    q.append((nx, ny, z+1))
                    
    return -1
print(bfs())
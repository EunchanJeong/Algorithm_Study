from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[-1] * m for _ in range(n)]
start = None

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(m):
        if row[j] == 2:
            start = (i, j)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(start):
    q = deque([start])
    visited[start[0]][start[1]] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = 0

bfs(start)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            visited[i][j] = 0

for row in visited:
    print(' '.join(map(str, row)))
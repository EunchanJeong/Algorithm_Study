import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

direction = [(1,0), (0,1), (-1,0), (0,-1)]
visit = [[0]*m for _ in range(n)]

def bfs(x, y):

    queue = deque([(x,y)])
    
    size = 1

    direction = [(1,0), (0,1), (-1,0), (0,-1)]
    while queue:
        x, y = queue.popleft()
        visit[x][y] = 1

        for dx, dy in direction:
            nx, ny = x+dx, y+dy

            if (nx >= 0 and nx < n) and (ny >= 0 and ny < m):
                if graph[nx][ny] == 1 and visit[nx][ny] != 1:
                    size += 1
                    visit[nx][ny] = 1
                    queue.append((nx, ny))
    return size

count = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visit[i][j] != 1:
            count += 1
            max_size = max(max_size, bfs(i, j))

print(count)
print(max_size)
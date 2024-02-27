from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

direction = [(1,0), (0,1), (-1,0), (0,-1)]

while queue:
    x, y = queue.popleft()

    for dx, dy in direction:
        nx, ny = x+dx, y+dy

        if (nx >= 0 and nx < N) and (ny >= 0 and ny < M):
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))

if any(0 in g for g in graph):
    print(-1)
else:
    print(max(map(max, graph))-1)
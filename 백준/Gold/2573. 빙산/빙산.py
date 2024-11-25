from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
ice = []
for i in range(N):
    graph.append(list(map(int, input().split())))

    for j in range(M):
        if graph[i][j] > 0:
            ice.append((i, j))

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0:
                    if graph[nx][ny] == 0 and graph[x][y] > 0:
                        graph[x][y] -= 1
                    elif graph[nx][ny] > 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny))

year = 0
check = 0
while ice:
    visited = [[0] * M for _ in range(N)]
    melt = []
    count = 0

    for x, y in ice:
       if graph[x][y] > 0 and visited[x][y] == 0:
           bfs(x, y, visited)
           count += 1

       if graph[x][y] == 0:
           melt.append((x, y))
    if count > 1:
        print(year)
        check = 1
        break
    year += 1
    ice = list(set(ice) - set(melt))
    ice.sort()

if not check:
    print(0)
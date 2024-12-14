from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*N for _ in range(N)]
count = 1
answer = int(1e9)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def bfs_island(x, y):
    global count

    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    graph[x][y] = count

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = 1
                    graph[nx][ny] = count
                    q.append((nx, ny))

def bfs_shortcut(island):
    global answer
    dist = [[-1]*N for _ in range(N)]

    q = deque()

    for i in range(N):
        for j in range(N):
            if graph[i][j] == island:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > 0 and graph[nx][ny] != island:
                    answer = min(answer, dist[x][y])
                    return
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

for i in range(N):
    for j in range(N):
        if visited[i][j] == -1 and graph[i][j] == 1:
            bfs_island(i, j)
            count += 1

for i in range(1, count):
    bfs_shortcut(i)

print(answer)
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 0

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs():
    global result

    visited = [[0] * M for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))

    safe_count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0 and not visited[i][j]:
                safe_count += 1

    result = max(result, safe_count)

def wall(count):
    if count == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(count + 1)
                graph[i][j] = 0

wall(0)
print(result)
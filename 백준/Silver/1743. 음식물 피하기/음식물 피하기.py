from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

graph = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
g = []
for _ in range(K):
    r, c = map(int, input().split())

    graph[r-1][c-1] = 1
    g.append((r-1, c-1))

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def bfs(start):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 1
    count = 1
    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    count += 1
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    return count

result = 0

for start in g:
    if visited[start[0]][start[1]] == 0:
        result = max(result, bfs(start))

print(result)
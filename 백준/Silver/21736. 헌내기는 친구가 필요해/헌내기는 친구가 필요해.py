from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
start = (0, 0)
visited = [[0] * M for _ in range(N)]
for i in range(N):
    row = list(input().strip())
    graph.append(row)
    for j in range(M):
        if row[j] == 'I':
            start = (i, j)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def bfs(v):
    q = deque()
    q.append(v)
    visited[v[0]][v[1]] = 1

    count = 0
    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0:
                    if graph[nx][ny] == 'P':
                        count += 1
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                    elif graph[nx][ny] == 'O':
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                    else:
                        continue
    return count

result = bfs(start)

if result == 0:
    print("TT")
else:
    print(result)
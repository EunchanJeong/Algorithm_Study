from collections import deque
import sys
input = sys.stdin.readline

directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def bfs(x, y):
    q = deque()

    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < w and 0 <= ny < h and graph[nx][ny] == 1:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

while True:
    h, w = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(w)]
    visited = [[-1] * h for _ in range(w)]

    count = 0
    for i in range(w):
        for j in range(h):
            if visited[i][j] == -1 and graph[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

x, y = r, c
visited[x][y] = 1
count = 1

while True:
    cleaned = False
    for _ in range(4):
        d = (d + 3) % 4
        nx, ny = x + directions[d][0], y + directions[d][1]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            x, y = nx, ny
            count += 1
            cleaned = True
            break
    if not cleaned:
        nx, ny = x - directions[d][0], y - directions[d][1]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 1:
            x, y = nx, ny
        else:
            break

print(count)
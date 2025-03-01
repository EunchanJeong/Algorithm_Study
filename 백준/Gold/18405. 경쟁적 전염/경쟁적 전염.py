from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

S, X, Y = map(int, input().split())

visited  = [[0] * N for _ in range(N)]

def search_dot(graph):
    q = deque()

    for n in range(1, K+1):
        for i in range(N):
            for j in range(N):
                if graph[i][j] == n:
                    q.append((i, j, n))
                    visited[i][j] = 1

    return q

def bfs(graph):
    q = search_dot(graph)

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    stop = 0
    while q:
        x, y, n = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    graph[nx][ny] = n
                    q.append((nx, ny, n))

                    if visited[x][y] + 1 > S:
                        stop = 1
                        break

                    visited[nx][ny] = visited[x][y] + 1
        if stop == 1:
            break

bfs(graph)
print(graph[X-1][Y-1])
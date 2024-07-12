
from collections import deque
T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph, x, y):
    queue = deque()
    queue.append([x, y])
    graph[y][x] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx >= 0 and nx < M) and (ny >= 0 and ny < N):
                if graph[ny][nx] == 1:
                    queue.append([nx, ny])
                    graph[ny][nx] = 0


for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0]*(M) for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(graph, j, i)
                count += 1
    print(count)
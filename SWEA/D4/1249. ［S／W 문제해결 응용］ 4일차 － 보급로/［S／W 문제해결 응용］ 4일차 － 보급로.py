from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(a, b):
    q = deque()
    q.append((a, b))
    result[a][b] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if result[x][y] + graph[nx][ny] < result[nx][ny]:
                    result[nx][ny] = result[x][y] + graph[nx][ny]
                    q.append((nx, ny))
T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    graph = []
    for _ in range(N):
        graph.append(list(map(int, input())))

    result = [[float('inf') for i in range(N)] for j in range(N)]
    bfs(0, 0)

    print(f"#{test_case} {result[N-1][N-1]}")
from collections import deque

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(x, y, N):
    q = deque()
    q.append((x, y))

    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        if graph[x][y] == "3":
            return visited[x][y]-2

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != "1":
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    graph = []
    visited = [[0] * N for _ in range(N)]

    q = deque()

    x, y = 0, 0
    for i in range(N):
        l = list(input())

        if "2" in l:
            x, y = i, l.index("2")

        graph.append(l)

    result = bfs(x, y, N)

    print(f"#{test_case} {result if result else 0}")
from collections import deque

T = int(input())

directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0

    while q:
        x, y = q.popleft()

        if x == end_x and y == end_y:
            return graph[x][y]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


for _ in range(T):
    N = int(input())

    graph = [[0]*(N) for _ in range(N)]

    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    print(bfs(start_x, start_y))
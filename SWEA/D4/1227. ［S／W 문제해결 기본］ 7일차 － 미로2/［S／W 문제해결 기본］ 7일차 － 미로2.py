from collections import deque

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(10):
    test_case = int(input())

    graph = []
    visited = [[False] * 100 for t in range(100)]

    for i in range(100):
        graph.append(list(input()))

    q = deque()
    q.append((1, 1))
    visited[1][1] = True

    result = 0
    while q and result == 0:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < 100) and  (0 <= ny < 100) and not visited[nx][ny]:
                if graph[nx][ny] == "0":
                    q.append((nx, ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] == "3":
                    result = 1
                    break

    print(f"#{test_case} {result}")
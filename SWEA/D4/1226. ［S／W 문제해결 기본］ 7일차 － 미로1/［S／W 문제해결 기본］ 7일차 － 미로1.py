directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def dfs(x, y):
    if graph[x][y] == "3":
        return 1

    result = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny]:
            if graph[nx][ny] != "1":
                visited[nx][ny] = True

                result = dfs(nx, ny)
                if result == 1:
                    break

                visited[nx][ny] = False

    return result


for _ in range(10):
    test_case = int(input())

    graph = []
    visited = [[False] * 16 for x in range(16)]

    for i in range(16):
        graph.append(list(input()))
    visited[1][1] = True
    result = dfs(1, 1)

    print(f"#{test_case} {result}")
T = int(input())

for t in range(1, T + 1):
    n = int(input())

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    graph = [[0] * n for _ in range(n)]
    num = 1
    d = 0

    x = 0
    y = -1
    while num <= (n * n):
        nx = x + directions[d][0]
        ny = y + directions[d][1]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = num
            num += 1
            x, y = nx, ny
        else:
            d = (d + 1) % 4

    print(f'#{t}')
    for g in graph:
        print(' '.join(map(str, g)))
def ladder(s):
    x, y = s[0], s[1]

    visited = [[False] * 100 for _ in range(100)]
    visited[x][y] = True

    while x < 99:
        if y > 0 and graph[x][y-1] != 0 and not visited[x][y-1]:
            while y > 0 and graph[x][y-1] != 0:
                y -= 1
                visited[x][y] = True

                if graph[x][y] == 2:
                    return s[1]

        elif y < 99 and graph[x][y + 1] != 0 and not visited[x][y + 1]:
            while y < 99 and graph[x][y + 1] != 0:
                y += 1
                visited[x][y] = True

                if graph[x][y] == 2:
                    return s[1]

        if graph[x+1][y] != 0:
            x += 1
            visited[x][y] = True

            if graph[x][y] == 2:
                return s[1]

    return 100

for _ in range(10):
    test_case = int(input())

    l = list(map(int, input().split()))

    starts = []
    for i in range(len(l)):
        if l[i] == 1:
            starts.append((0, i))

    graph = []
    graph.append(l)

    for i in range(99):
        graph.append(list(map(int, input().split())))

    for s in starts:
        result = ladder(s)
        if result != 100:
            print(f"#{test_case} {result}")
            break
from collections import deque

directions = [(0, -1), (0, 1), (1, 0)]

def ladder(s):
    x, y = s[0], s[1]
    count = 0
    visited = [[False] * 100 for _ in range(100)]
    visited[x][y] = True

    while x < 99:
        if y > 0 and graph[x][y-1] == 1 and not visited[x][y-1]:
            while y > 0 and graph[x][y-1] == 1:
                y -= 1
                count += 1
                visited[x][y] = True
        elif y < 99 and graph[x][y+1] == 1 and not visited[x][y+1]:
            while y < 99 and graph[x][y+1] == 1:
                y += 1
                count += 1
                visited[x][y] = True

        x += 1
        count += 1
        visited[x][y] = True

    return (s[1], count)

for _ in range(10):
    test_case = int(input())

    graph = []
    starts = []
    result = []

    l = list(map(int, input().split()))
    graph.append(l)

    for i in range(len(l)):
        if l[i] == 1:
            starts.append((0, i))

    for i in range(99):
        l = list(map(int, input().split()))
        graph.append(l)

    for s in starts:
        result.append(ladder(s))

    result.sort(key=lambda x : [x[1], x[0]])
    print(f"#{test_case} {result[0][0]}")
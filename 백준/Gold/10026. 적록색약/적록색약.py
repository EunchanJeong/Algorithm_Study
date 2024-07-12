from collections import deque

N = int(input())

count1 = 0
count2 = 0

graph = []
visited1 = [[0]*(N) for _ in range(N)]
visited2 = [[0]*(N) for _ in range(N)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs1(graph, x, y):
    queue = deque()
    queue.append([x, y])
    visited1[y][x] = 1
    check = graph[y][x]

    while queue:
        x, y = queue.popleft()

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            if (nx >= 0 and nx < N) and (ny >= 0 and ny < N):
                if visited1[ny][nx] != 1 and graph[ny][nx] == check:
                    queue.append([nx, ny])
                    visited1[ny][nx] = 1

    
def bfs2(graph, x, y):
    queue = deque()
    queue.append([x, y])
    visited2[y][x] = 1
    check = graph[y][x]

    if check == 0 or check == 1:
        while queue:
            x, y = queue.popleft()

            for dx, dy in direction:
                nx = x + dx
                ny = y + dy

                if (nx >= 0 and nx < N) and (ny >= 0 and ny < N):
                    if visited2[ny][nx] != 1 and (graph[ny][nx] == 0 or graph[ny][nx] == 1):
                        queue.append([nx, ny])
                        visited2[ny][nx] = 1
    else:
        while queue:
            x, y = queue.popleft()

            for dx, dy in direction:
                nx = x + dx
                ny = y + dy

                if (nx >= 0 and nx < N) and (ny >= 0 and ny < N):
                    if visited2[ny][nx] != 1 and graph[ny][nx] == check:
                        queue.append([nx, ny])
                        visited2[ny][nx] = 1

    



for _ in range(N):
    tmp = []
    
    for i in list(input()):
        if i == 'R':
            tmp.append(0)
        elif i == 'G':
            tmp.append(1)
        else:
            tmp.append(2)
        
    graph.append(tmp)

for x in range(N):
    for y in range(N):
        if visited1[y][x] != 1:
            bfs1(graph, x, y)
            count1 += 1
        if visited2[y][x] != 1:
            bfs2(graph, x, y)
            count2 += 1

print(count1, count2)
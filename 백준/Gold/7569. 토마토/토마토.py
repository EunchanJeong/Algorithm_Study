from collections import deque

M, N, H = map(int, input().split())
graph = []
queue = deque()

directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

for i in range(H):
    tmp1 = []
    for j in range(N):
        tmp2 = list(map(int, input().split()))
        tmp1.append(tmp2)
        for idx, value in enumerate(tmp2):
            if value == 1:
                queue.append([idx, j, i])
    graph.append(tmp1)

while queue:
    x, y, z = queue.popleft()
    for dx, dy, dz in directions:
        nx, ny, nz = x + dx, y + dy, z + dz
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and graph[nz][ny][nx] == 0:
            graph[nz][ny][nx] = graph[z][y][x] + 1
            queue.append([nx, ny, nz])

max_day = 0
is_all_ripe = True
for g in graph:
    for l in g:
        if 0 in l:  
            is_all_ripe = False
        max_day = max(max_day, max(l))

if is_all_ripe:
    print(max_day - 1)  
else:
    print(-1)

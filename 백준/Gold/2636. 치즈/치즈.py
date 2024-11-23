import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())

graph = []
point = []

for i in range(R):
    row = list(map(int, input().split()))
    graph.append(row)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs():
    visited = [[0] * C for _ in range(R)]
    q = deque()
    q.append((0, 0))
    count = 0
    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    count += 1
    return count

time = 0
result = []
while True:
    cnt = bfs()
    result.append(cnt)

    if cnt == 0:
        break
    time += 1
    
print(time)
print(result[-2])
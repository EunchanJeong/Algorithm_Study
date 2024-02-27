from collections import deque
import sys
# input = sys.stdin.readline

n, m = map(int, input().split())

graph =[]
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

count = 0
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy

            if (nx >= 0 and nx < n) and (ny >= 0 and ny < m):
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
    return graph[n-1][m-1]

print(bfs(0, 0))
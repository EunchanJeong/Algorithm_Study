from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ladders = {}
snakes = {}

for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snakes[u] = v

graph = [0] * 101
visited = [0] * 101
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        position = q.popleft()

        if position == 100:
            break

        for i in range(1, 7):
            np = position + i

            if 0 <= np <= 100 and visited[np] == 0:
                if np in ladders:
                    np = ladders[np]
                if np in snakes:
                    np = snakes[np]

                if visited[np] == 0:
                    q.append(np)
                    visited[np] = 1
                    graph[np] = graph[position] + 1

bfs(1)
print(graph[100])

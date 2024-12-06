from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

def bfs(node):
    visited = [0] * (N+1)

    q = deque()
    q.append(node)
    visited[node] = 1
    count = 0
    while q:
        n = q.popleft()

        for i in graph[n]:
            if visited[i] == 0 and i != node:
                visited[i] = visited[n] + 1
                q.append(i)
    return sum(visited)

result = 1e9
min_kevin = 0
for i in range(1, N+1):
    step = bfs(i)

    if step < result:
        result = step
        min_kevin = i

print(min_kevin)
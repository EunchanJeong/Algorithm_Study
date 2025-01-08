from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()
def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    count = 2
    while q:
        n = q.popleft()

        for t in graph[n]:
            if visited[t] == 0:
                q.append(t)
                visited[t] = count
                count += 1

bfs(R)

for v in visited[1:]:
    print(v)
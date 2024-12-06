from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

def bfs(node):
    q = deque()

    q.append(node)
    visited[node] = 1

    while q:
        v = q.popleft()

        for n in graph[v]:
            if visited[n] == 0:
                q.append(n)
                visited[n] = 1

count = 0
for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        count += 1
print(count)
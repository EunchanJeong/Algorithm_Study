from collections import deque
import sys
input = sys.stdin.readline

def dfs(node):
    visited[node] = 1
    print(node, end=' ')

    for v in graph[node]:
        if visited[v] == 0:
            dfs(v)


def bfs():
    visited = [0] * (N+1)

    q = deque()
    q.append(V)
    visited[V] = 1

    while q:
        node = q.popleft()
        print(node, end=' ')
        for v in graph[node]:
            if visited[v] == 0:
                q.append(v)
                visited[v] = 1

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for g in graph:
    g.sort()

visited = [0] * (N+1)
dfs(V)
print()
bfs()
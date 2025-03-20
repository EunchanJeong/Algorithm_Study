from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end):
    q = deque()

    q.append((start, 0))

    visited = [False] * (N+1)

    visited[start] = True

    while q:
        v, d = q.popleft()

        if v == end:
            return d

        for i, l in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append((i, d + l))

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    n1, n2, l = map(int, input().split())
    graph[n1].append((n2, l))
    graph[n2].append((n1, l))

for _ in range(M):
    n1, n2 = map(int, input().split())

    print(bfs(n1, n2))
from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort(reverse=True)

visited = [0] * (N+1)

def bfs(r):
    q = deque()
    q.append(r)
    visited[r] = 1
    count = 1
    while q:
        v = q.popleft()

        for n in graph[v]:
            if(visited[n] == 0):
                q.append(n)
                count += 1
                visited[n] = count


bfs(R)
for v in visited[1:]:
    print(v)
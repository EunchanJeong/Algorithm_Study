from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        n = q.popleft()

        for t in graph[n]:
            if visited[t] == 0:
                q.append(t)
                visited[t] = visited[n] + 1

bfs(1)

count = 0
for i in range(2, n+1):
    if 1 <= visited[i] <= 3:
        count += 1
print(count)
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
result = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort(reverse=True)

count = 1
def dfs(v):
    global count
    visited[v] = 1
    result[v] = count

    for n in graph[v]:
        if visited[n] == 0:
            count += 1
            dfs(n)

dfs(R)

for r in result[1:]:
    print(r)
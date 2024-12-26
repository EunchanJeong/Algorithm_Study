import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
order = [0] * (N + 1)
count = 1

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort()

def dfs(v):
    global count
    visited[v] = 1
    order[v] = count
    count += 1

    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(next_node)

dfs(R)

for i in range(1, N + 1):
    print(order[i])
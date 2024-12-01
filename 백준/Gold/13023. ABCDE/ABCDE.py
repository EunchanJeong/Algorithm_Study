import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

def dfs(node, visited, count):
    global check
    if count == 4:
        check = 1
        return

    visited[node] = 1
    for n in graph[node]:
        if visited[n] == 0:
            dfs(n, visited, count+1)
    visited[node] = 0

check = 0
for i in range(N):
    count = 0
    visited = [0] * N

    dfs(i, visited, count)

    if check == 1:
        print(check)
        break

if check == 0:
    print(check)
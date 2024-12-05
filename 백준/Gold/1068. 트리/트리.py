import sys
input = sys.stdin.readline

N = int(input())
parents = list(map(int, input().split()))
delete = int(input())

graph = [[] for _ in range(N)]
for i in range(N):
    if parents[i] != -1 and i != delete:
        graph[parents[i]].append(i)

def dfs(node):
    while graph[node]:
        d = graph[node].pop()
        dfs(d)
    graph[node].append(-2)

dfs(delete)

count = 0
for i in range(N):
    if not graph[i]:
        count += 1

print(count)
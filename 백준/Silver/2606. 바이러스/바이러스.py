from collections import deque

C = int(input())
N = int(input())

graph = [[] for _ in range(C+1)]
visited = [0] * (C+1)

for _ in range(N):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    count = 0
    while q:
        node = q.popleft()
        for n_node in graph[node]:
            if visited[n_node] == 0:
                visited[n_node] = 1
                count += 1
                q.append(n_node)
            
    print(count)
    
bfs(1)
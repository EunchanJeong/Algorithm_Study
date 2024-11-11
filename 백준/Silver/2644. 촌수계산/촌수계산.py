from collections import deque

n = int(input())
a, b = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    p, c = map(int, input().split())
    
    graph[p].append(c)
    graph[c].append(p)
    
def bfs(a, b):
    
    q = deque()
    q.append(a)
    visited[a] = 0
    
    while q:
        t = q.popleft()
        
        if t == b:
            return visited[b]

        for g in graph[t]:
            if visited[g] == 0:
                q.append(g)
                visited[g] = visited[t] + 1
    return -1

print(bfs(a, b))
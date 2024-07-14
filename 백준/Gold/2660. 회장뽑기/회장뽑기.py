from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
visit_score = []

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(n):
    visited = [-1] * (N+1)
    
    visited[n] = 0
    
    queue = deque()
    queue.append((n))
    
    while queue:
        v = queue.popleft()
        for x in graph[v]:
            if visited[x] == -1:
                visited[x] = visited[v] + 1
                queue.append(x)
    return max(visited)


for n in range(1, N+1):
    visit_score.append(bfs(n))


visit_min = min(visit_score)
c = [i+1 for i, score in enumerate(visit_score) if score == visit_min]

print(visit_min, len(c))
print(' '.join(map(str, c)))
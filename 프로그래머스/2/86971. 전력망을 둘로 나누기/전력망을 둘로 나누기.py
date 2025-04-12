from collections import deque

def bfs(s, e, visited, graph):
    visited[s] = 1
    visited[e] = 1
    
    q = deque()
    q.append(e)
    
    count = 1
    while q:
        cur = q.popleft()
        
        for next in graph[cur]:
            if visited[next] == 0:
                visited[next] = 1
                count += 1
                q.append(next)
        
    return count

def solution(n, wires):
    answer = -1
    
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    answer = float('inf')
    
    for a, b in wires:
        visited = [0] * (n+1)
        count = bfs(a, b, visited, graph)
        
        d = abs(n - count)
        count = abs(count - d)
        
        answer = min(answer, count)
    return answer
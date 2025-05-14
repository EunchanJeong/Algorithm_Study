from collections import deque

def dfs(node, graph):
        count = 1
        
        for idx in graph[node]:
            count += dfs(idx, graph)
            
        return count
    
T = int(input())

for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    
    nodes = list(map(int, input().split()))
    max_node = max(nodes)  
    
    graph = [[] for _ in range(max_node+1)]
    
    for i in range(0, len(nodes), 2):
        parent, child = nodes[i], nodes[i+1]
        graph[parent].append(child)
    
    count = dfs(N, graph)
  
    print(f"#{test_case} {count}")
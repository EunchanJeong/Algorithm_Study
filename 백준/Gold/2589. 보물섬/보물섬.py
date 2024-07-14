from collections import deque

H, W = map(int, input().split())
graph = []

start_q = deque()

for h in range(H):
    tmp = list(input())
    
    for w, value in enumerate(tmp):
        if value == 'L':
            start_q.append((w, h))
    graph.append(tmp)

visit_count = 0


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(x, y):
    visited = [[0]*(W) for _ in range(H)]
    
    visited[y][x] = 1
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if((nx >= 0 and nx < W) and (ny >= 0 and ny < H) and graph[ny][nx] == 'L' and visited[ny][nx] == 0):
                visited[ny][nx] = visited[y][x] + 1
                queue.append((nx, ny))
    
    return max(map(max, visited))

while start_q:
    s_x, s_y = start_q.popleft()
    
    t = bfs(s_x, s_y)
    
    if visit_count < t:
        visit_count =  t

print(visit_count-1)
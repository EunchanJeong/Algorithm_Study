from collections import deque
import sys

N = int(input())
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def bfs_f():
    fire_size = len(fire_q)
    for _ in range(fire_size):
        x, y = fire_q.popleft()
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                fire_q.append((nx, ny))

def bfs_p(start):
    person_q = deque([start])
    visit[start[1]][start[0]] = 1
    
    while person_q:
        bfs_f()
        
        person_size = len(person_q)
        for _ in range(person_size):
            x, y = person_q.popleft()
            
            if x == 0 or x == w - 1 or y == 0 or y == h - 1:
                return visit[y][x]
            
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                
                if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] != -1:
                    if (graph[ny][nx] == 0 or visit[y][x] + 1 < graph[ny][nx]) and visit[ny][nx] == 0:
                        visit[ny][nx] = visit[y][x] + 1
                        person_q.append((nx, ny))
                        
    return 'IMPOSSIBLE'

for _ in range(N):
    w, h = map(int, sys.stdin.readline().split())
    
    graph = [[0] * w for _ in range(h)]
    visit = [[0] * w for _ in range(h)]
    fire_q = deque()
    
    for i in range(h):
        tmp = sys.stdin.readline().strip()
        
        for j in range(w):
            if tmp[j] == '#':
                graph[i][j] = -1
            elif tmp[j] == '*':
                graph[i][j] = 1
                fire_q.append((j, i))
            elif tmp[j] == '.':
                graph[i][j] = 0
            else:
                graph[i][j] = 0
                start = (j, i)
    
    result = bfs_p(start)
    print(result)
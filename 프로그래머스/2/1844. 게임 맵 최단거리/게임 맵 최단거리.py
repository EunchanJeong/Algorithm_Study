from collections import deque

def solution(maps):
    answer = 0
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        
        while q:
            x, y = q.popleft()
            
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                if maps[nx][ny] == 0:
                    continue
                
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
        return maps[len(maps)-1][len(maps[0])-1]
    
    answer = bfs(0, 0)
    
    if answer == 1:
        return -1
    else:
        return answer
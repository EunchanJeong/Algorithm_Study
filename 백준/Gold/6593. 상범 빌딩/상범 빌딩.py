from collections import deque

directions =[(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
def bfs(start):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]][start[2]] = 1
    
    while q:
        x, y, z = q.popleft()
        
        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz
            
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C:
                if graph[nx][ny][nz] == 'E':
                    print(f'Escaped in {visited[x][y][z]} minute(s).')
                    return
                elif graph[nx][ny][nz] == '.' and visited[nx][ny][nz] == 0:
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    q.append((nx, ny, nz))
    print('Trapped!')
              
                
while True:
    L, R, C = map(int, input().split())
    
    if L == 0 and R == 0 and C == 0:
        break

    graph = [[[] for _ in range(R)] for _ in range(L)]
    visited = [[[0]*C for _ in range(R)] for _ in range(L)]
    
    for i in range(L):
        graph[i] = [list(map(str, input().strip())) for _ in range(R)]
        input()
    
    for i in range(L):
        for j in  range(R):
            for k in range(C):
                if graph[i][j][k] == 'S':
                    bfs((i, j, k))
                    break
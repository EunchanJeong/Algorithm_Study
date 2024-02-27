from collections import deque
import sys
input = sys.stdin.readline

direction = [(1,0), (0,1), (-1,0), (0,-1)]

def F_bfs(queue):
    while queue:
        x, y = queue.popleft()

        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if not ((nx >= 0 and nx < R) and (ny >= 0 and ny < C)):
                continue
            if maze[nx][ny] == '#' or F_map[nx][ny]:
                continue

            F_map[nx][ny] = F_map[x][y]+1
            queue.append((nx, ny))

def J_bfs(queue):
    while queue:
        x, y = queue.popleft()

        for dx, dy in direction:

            nx, ny = x+dx, y+dy

            if not((nx >= 0 and nx < R) and (ny >= 0 and ny < C)):
                print(J_map[x][y])
                return
            
            if maze[nx][ny] == '#' or J_map[nx][ny]:
                continue
            if F_map[nx][ny] and J_map[x][y]+1 >= F_map[nx][ny]:
                continue

            J_map[nx][ny] = J_map[x][y]+1
            queue.append((nx, ny))

    print('IMPOSSIBLE')
    return
          
R, C = map(int, input().split())

maze = []
J_map = [[0]*C for _ in range(R)]
F_map = [[0]*C for _ in range(R)]

J_queue = deque()
F_queue = deque()

for _ in range(R):
    maze.append(input().rstrip())

for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            J_queue.append((i, j))
            J_map[i][j] = 1
        elif maze[i][j] == 'F':
            F_queue.append((i, j))
            F_map[i][j] = 1


F_bfs(F_queue)
J_bfs(J_queue)
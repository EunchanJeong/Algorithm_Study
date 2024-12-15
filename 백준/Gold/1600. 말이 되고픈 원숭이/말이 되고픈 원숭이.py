from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
W, H = map(int,input().split())

graph =[list(map(int, input().split())) for _ in range(H)]

visited =[[[-1]*(K+1) for _ in range(W)] for _ in range(H)]

horse = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
monkey = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))
    visited[x][y][z] = 0

    while q:
        x, y, z = q.popleft()
        if x == H-1 and y == W-1:
            return visited[x][y][z]

        if z > 0:
            for dx, dy in horse:
                nx, ny = x + dx, y + dy
                if 0 <= nx < H and 0 <= ny < W and visited[nx][ny][z-1] == -1:
                    if graph[nx][ny] == 0:
                        visited[nx][ny][z-1] = visited[x][y][z] + 1
                        q.append((nx, ny, z-1))

        for dx, dy in monkey:
            nx, ny = x + dx, y + dy

            if 0 <= nx < H and 0 <= ny < W and visited[nx][ny][z] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))
    return -1

print(bfs(0, 0, K))
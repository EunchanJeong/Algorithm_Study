from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(home)

    while q:
        x, y = q.popleft()

        if abs(festival_x - x) + abs(festival_y - y) <= 1000:
            print('happy')
            return
        else:
            for i in range(N):
                nx, ny = market[i]
                if visited[i] == 0:
                    if abs(nx - x) + abs(ny - y) <= 1000:
                        visited[i] = 1
                        q.append((nx, ny))
    print('sad')


T = int(input())
for _ in range(T):
    N = int(input())

    home = list(map(int, input().split()))

    market = []
    for _ in range(N):
        market.append(list(map(int, input().split())))

    festival_x, festival_y = list(map(int, input().split()))

    visited = [0] * (N)
    bfs()
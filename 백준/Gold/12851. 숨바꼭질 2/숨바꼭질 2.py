from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

visited = [-1] * 100001
count = 0

def bfs(N):
    global count

    q = deque()
    q.append(N)
    visited[N] = 0

    while q:
        x = q.popleft()
        if x == K:
            count += 1

        for nx in (x+1, x-1, 2*x):
            if 0 <= nx <= 100000 and (visited[nx] == -1 or visited[nx] >= visited[x] + 1):
                visited[nx] = visited[x] + 1
                q.append(nx)

bfs(N)
print(visited[K])
print(count)
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

def bfs(start):
    q = deque()
    q.append(start)
    
    while q:
        a = q.popleft()
        for i in range(N):
            if visited[start][i] == 0 and graph[a][i] == 1:
                q.append(i)
                visited[start][i] = 1
                
visited = [[0] * N for _ in range(N)]
for i in range(N):
    bfs(i)

for v in visited:
    print(' '.join(map(str, v)))
from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, k):
    queue = deque([n])

    while queue:
        x = queue.popleft()
        if x == k:
            print(array[x])
            return 
        
        for nx in (x+1, x-1, 2*x):
                if(nx >= 0 and nx < max_length) and (not array[nx]):
                    array[nx] = array[x]+1
                    queue.append(nx)


N, K = map(int, input().split())

max_length = 100001

array = [0]*max_length
bfs(N, K)
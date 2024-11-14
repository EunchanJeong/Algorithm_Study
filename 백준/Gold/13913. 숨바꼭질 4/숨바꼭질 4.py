from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

MAX =  100001
time = [-1] * MAX
previous = [-1] * MAX

def bfs(x, y):
    if x == y:
        print(0)
        print(x)
        return

    q = deque()

    q.append(x)
    time[x] = 0

    while q:
        x = q.popleft()

        if x == y:
            print(time[x])

            path = []
            while x != -1:
                path.append(x)
                x = previous[x]
            path.reverse()
            print(' '.join(map(str, path)))
            return

        for nx in (x-1, x+1, x*2):
            if 0 <= nx < MAX and time[nx] == -1:
                if nx == x * 2:
                    time[nx] = time[x] + 1
                    q.appendleft(nx)
                    previous[nx] = x
                else:
                    time[nx] = time[x] + 1
                    q.append(nx)
                    previous[nx] = x


bfs(N, K)
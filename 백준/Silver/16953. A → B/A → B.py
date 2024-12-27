from collections import deque
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

q = deque()
q.append((A, 1))

while q:
    n, count = q.popleft()

    if n > B:
        continue
    if n == B:
        print(count)
        break

    q.append((n * 2, count+1))
    q.append((int(str(n)+'1'), count + 1))
else:
    print(-1)
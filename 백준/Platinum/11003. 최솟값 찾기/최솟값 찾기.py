from collections import deque

D, L = map(int, input().split())
A = list(map(int, input().split()))
q = deque()

for i in range(D):
    while q and q[-1][1] > A[i]:
        q.pop()
    q.append((i, A[i]))
    
    if q[0][0] <= i-L:
        q.popleft()
    print(q[0][1], end=' ')
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

q = deque([i for i in range(1, N+1)])

result = []

idx = K
while q:
    for _ in range(K-1):
        q.append(q.popleft())

    result.append(q.popleft())

print('<' + ', '.join(map(str, result)) + '>')
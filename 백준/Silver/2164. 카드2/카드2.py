import sys
from collections import deque

N = int(sys.stdin.readline())

dequeue = deque([x for x in range(1, N+1)])

while len(dequeue) != 1:
    dequeue.popleft()
    dequeue.append(dequeue[0])
    dequeue.popleft()

print(dequeue[0])
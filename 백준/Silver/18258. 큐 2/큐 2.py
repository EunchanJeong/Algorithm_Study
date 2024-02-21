import sys
from collections import deque

N = int(sys.stdin.readline())

dequeue = deque()

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        dequeue.append(command[1])
    elif command[0] == 'pop':
        if len(dequeue) == 0:
            print(-1)
        else:
            print(dequeue.popleft())
    elif command[0] == 'size':
        print(len(dequeue))
    elif command[0] == 'empty':
        if len(dequeue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(dequeue) == 0:
            print(-1)
        else:
            print(dequeue[0])
    elif command[0] == 'back':
        if len(dequeue) == 0:
            print(-1)
        else:
            print(dequeue[-1])
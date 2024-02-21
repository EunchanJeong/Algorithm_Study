import sys
from collections import deque

N = int(sys.stdin.readline())
error = 0

for _ in range(N):
    reverse_flag = 0
    error = 0

    commands = sys.stdin.readline().rstrip()
    size = int(sys.stdin.readline())

    tmp = sys.stdin.readline().rstrip()[1:-1].split(',')
    dq = deque(tmp)
    if '' in tmp:
        dq.pop()

    for command in commands:
        if command == 'R':
            reverse_flag += 1
        elif command == 'D':
            if len(dq) == 0:
                print('error')
                error = 1
                break
            else:
                if reverse_flag % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
    
    if error == 1:
        continue
    else:
        if reverse_flag % 2 == 0:
            print('['+','.join(dq)+']')
        else:
            dq.reverse()
            print('['+','.join(dq)+']')
import sys
from collections import deque

inputs = list(map(int, sys.stdin.readline().split()))
deque = deque([x for x in range(1, inputs[0]+1)])

nums = list(map(int, sys.stdin.readline().split()))

count = 0

for num in nums:
    while True:
        if deque[0] == num:
            deque.popleft()
            break
        else:
            if deque.index(num) < len(deque)/2:
                while deque[0] != num:
                    deque.append(deque.popleft())
                    count += 1
            else:
                while deque[0] != num:
                    deque.appendleft(deque.pop())
                    count += 1

print(count)
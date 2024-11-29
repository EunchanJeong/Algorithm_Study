from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
belt = list(map(int, input().split()))

boxes = deque([0] * N)
idx = 0

while True:
    belt = [belt[-1]] + belt[:-1]
    boxes.rotate(1)
    boxes[-1] = 0  

    for i in range(N-2, -1, -1):  
        if boxes[i] == 1 and boxes[i+1] == 0 and belt[i+1] > 0:
            boxes[i] = 0
            boxes[i+1] = 1
            belt[i+1] -= 1
    boxes[-1] = 0 

    if belt[0] > 0:
        boxes[0] = 1
        belt[0] -= 1

    if belt.count(0) >= K:
        break

    idx += 1

print(idx+1)
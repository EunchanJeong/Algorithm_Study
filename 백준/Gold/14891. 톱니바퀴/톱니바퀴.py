from collections import deque
import sys
input = sys.stdin.readline

gears = []
for _ in range(4):
    gears.append(deque(list(map(int, input().strip()))))

K = int(input())
for _ in range(K):
    idx, direction = map(int, input().split())
    idx -= 1

    rotations = [0] * 4
    rotations[idx] = direction

    for i in range(idx, 3):
        if gears[i][2] != gears[i+1][6]:
            rotations[i+1] = -rotations[i]
        else:
            break

    for i in range(idx, 0, -1):
        if gears[i][6] != gears[i-1][2]:
            rotations[i-1] = -rotations[i]
        else:
            break

    for i in range(4):
        if rotations[i] != 0:
            gears[i].rotate(rotations[i])

result = 0
for i in range(4):
    if gears[i][0] == 1:
        result += 2**i

print(result)
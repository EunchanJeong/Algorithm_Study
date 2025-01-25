from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
nums = deque(enumerate(map(int, input().split()), start=1))

i = 0
result = []
while nums:
    idx, move = nums.popleft()
    result.append(idx)

    if not nums:
        break
    if move > 0:
        move -= 1
    nums.rotate(-move)
print(' '.join(map(str, result)))
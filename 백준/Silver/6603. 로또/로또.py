from itertools import combinations
import sys
input = sys.stdin.readline

def dfs(idx, depth):
    if depth == 6:
        tmp = [str(r) for r in result]
        print(' '.join(tmp))
        return

    for i in range(idx, size):
        result.append(nums[i])
        dfs(i+1, depth+1)
        result.pop()

while True:
    inputs = list(map(int, input().split()))
    size = inputs[0]
    if size == 0:
        break

    nums = inputs[1:]

    result = []
    dfs(0, 0)
    print()
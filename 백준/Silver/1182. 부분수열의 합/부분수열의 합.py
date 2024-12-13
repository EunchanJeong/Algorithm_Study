import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
result = []
def backtracking(start):
    global count

    if sum(result) == S and len(result) > 0:
        count += 1

    for i in range(start, N):
        result.append(nums[i])
        backtracking(i+1)
        result.pop()

backtracking(0)

print(count)
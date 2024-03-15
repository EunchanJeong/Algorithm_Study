import sys
input = sys.stdin.readline

N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()
nums.reverse()

for i in nums:
    print(i)
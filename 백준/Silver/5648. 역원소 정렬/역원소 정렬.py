import sys
input = sys.stdin.read

N, *nums = input().split()

for i in range(int(N)):
    nums[i] = nums[i][::-1]

nums = list(map(int, nums))
nums.sort()

for n in nums:
    print(n)
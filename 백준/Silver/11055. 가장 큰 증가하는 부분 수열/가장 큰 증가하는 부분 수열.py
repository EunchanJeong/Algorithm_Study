import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = nums.copy()

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], nums[i] + dp[j])

print(max(dp))
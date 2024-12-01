import sys
input = sys.stdin.readline

nums = list(input().split('-'))


for i in range(len(nums)):
    nums[i] = sum(map(int, nums[i].split('+')))

result = nums[0]
for num in nums[1:]:
    result -= num
print(result)
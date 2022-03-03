size = int(input())
nums = list(map(int, input().split()))

max_num = nums[0]
min_num = nums[0]

for i in range(1, len(nums)):
    if nums[i] > max_num:
        max_num = nums[i]
    if nums[i] < min_num:
        min_num = nums[i]

print(min_num, max_num)
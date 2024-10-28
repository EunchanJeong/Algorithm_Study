N = int(input())
nums = {}
for _ in range(N):
    n = int(input())
    
    if n in nums:
        nums[n] += 1
    else:
        nums[n] = 1

max_count = max(nums.values())

result = min(key for key, value in nums.items() if value == max_count)

print(result)
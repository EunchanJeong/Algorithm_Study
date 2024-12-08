import sys
input = sys.stdin.readline

nums = list(input().strip())
nums = sorted(nums, reverse=True)

if '0' not in nums:
    print(-1)
else:
    if sum(map(int, nums)) % 3 != 0:
        print(-1)
    else:
        print(''.join(nums))
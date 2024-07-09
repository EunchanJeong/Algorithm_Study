def binary_search(t, nums):
    s = 0
    e = len(nums)-1

    while(s <= e):
        mid = (s+e)//2

        if nums[mid] > t:
            e = mid - 1
        elif nums[mid] < t:
            s = mid + 1
        else:
            return 1
    return 0

N = int(input())

nums = list(map(int, input().split()))
nums.sort()

M = int(input())

targets = list(map(int, input().split()))

for target in targets:
    print(binary_search(target, nums))
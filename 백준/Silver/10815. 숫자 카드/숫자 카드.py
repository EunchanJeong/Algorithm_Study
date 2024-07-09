def binary_search(t, nums):
    s = 0
    e = len(nums)-1
    
    while(s <= e):
        mid = (s+e)//2
        
        if t < nums[mid]:
            e = mid-1
        elif t > nums[mid]:
            s = mid+1
        else:
            return 1
    return 0
    
N = int(input())
nums = list(map(int, input().split()))
nums.sort()

M = int(input())
targets = list(map(int, input().split()))

result = []
for target in targets:
    result.append(binary_search(target, nums))
    
for i in result:
    print(i, end=' ')
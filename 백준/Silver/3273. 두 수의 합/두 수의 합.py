n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums.sort()

count = 0

i = 0
j = len(nums)-1

while i < j:
    tmp = nums[i] + nums[j]
    
    if tmp == x:
        i += 1
        j -= 1
        count += 1
    elif tmp < x:
        i += 1
    else:
        j -= 1
        
print(count)
    


room_num = input()

nums = [0 for x in range(0, 9)]

for i in room_num:
    if i == '9':
        i = '6'
    nums[int(i)] += 1
    
if nums[6] > 1:
    tmp = nums[6]//2
    if nums[6]%2 == 0:
        nums[6] = tmp
    else:
        nums[6] = tmp+1
        
print(max(nums))

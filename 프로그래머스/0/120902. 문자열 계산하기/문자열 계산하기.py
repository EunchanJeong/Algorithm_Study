def solution(my_string):
    my_string = my_string.split()
    
    nums = []
    t = []
    for s in my_string:
        if s.isdigit():
            nums.append(int(s))
            
            if len(nums) == 2:
                k = t.pop()
                
                n2 = nums.pop()
                n1 = nums.pop()
                if k == '+':
                    nums.append(n1+n2)
                else:
                    nums.append(n1-n2)
        else:
            t.append(s)
    return nums[0]
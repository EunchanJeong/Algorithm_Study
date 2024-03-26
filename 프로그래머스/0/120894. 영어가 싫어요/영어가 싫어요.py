def solution(numbers):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    dic_nums = {}
    count = 0
    for n in nums:
        dic_nums[n] = str(count)
        count += 1
    
    for key, value in dic_nums.items():
        numbers = numbers.replace(key, value)
    
    return int(numbers)
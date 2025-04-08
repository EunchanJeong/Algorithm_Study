import math

def convert(n, q):
    rev_base = ''
    
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    
    return rev_base[::-1]

def is_prime_number(x):
    if x == 1:
        return False
    
    for i in range (2, int(math.sqrt(x)) + 1):
    	if x % i == 0:
        	return False
    return True


def solution(n, k):
    num = convert(n, k)
    
    nums = list(num.split('0'))
    
    while nums.count('') > 0:
        nums.pop(nums.index(''))
    
    count = 0
    
    for n in nums:
        if is_prime_number(int(n)):
            count += 1
            
    return count
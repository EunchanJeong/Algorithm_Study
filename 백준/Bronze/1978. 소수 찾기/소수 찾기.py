n = int(input())
nums = map(int, input().split())
prime_count = 0
for num in nums:
    error = 0
    if num > 1 :
        for i in range(2, num):
            if num % i == 0:
                error += 1
        if error == 0:
            prime_count += 1
print(prime_count)
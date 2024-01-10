A = int(input())
B = int(input())
C = int(input())

result = A*B*C

nums = {}

for i in range(0, 10):
    nums[str(i)] = 0
for num in str(result):
    nums[num] += 1

for i in nums.values():
    print(i)
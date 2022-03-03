size, X = map(int, input().split())

nums = list(map(int, input().split()))

smalls = []

for i in range(size):
    if(nums[i] < X):
        print(nums[i], "", end='')
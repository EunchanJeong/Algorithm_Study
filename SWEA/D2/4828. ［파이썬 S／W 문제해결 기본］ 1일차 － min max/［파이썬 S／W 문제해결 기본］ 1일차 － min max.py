T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = max(nums) - min(nums)
    
    print(f"#{test_case} {result}")
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    result = []
    for i in range(N - M + 1):
        result.append(sum(nums[i:i + M]))

    print(f"#{test_case} {max(result) - min(result)}")
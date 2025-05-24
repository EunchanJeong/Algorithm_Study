T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))

    index = 0
    for _ in range(K):
        index += M

        if index == len(nums):
            nums.append(nums[-1] + nums[0])
        else:
            index = index % len(nums)
            prev = nums[index - 1] if index != 0 else nums[-1]
            curr = nums[index]
            nums.insert(index, prev + curr)

    result = nums[::-1][:10]
    print(f"#{test_case} {' '.join(map(str, result))}")
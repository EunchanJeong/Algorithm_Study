N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums = list(set(nums))
nums.sort()

arr = [0 for _ in range(M)]

def backtracking(k):
    if k == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(len(nums)):
        arr[k] = nums[i]
        backtracking(k+1)

backtracking(0)
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = list(set(nums))
nums.sort()
isused = [False for _ in range(N)]
arr = [0 for _ in range(M)]

def backtracking(k, start):
    if k == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(start, len(nums)):
            arr[k] = nums[i]
            backtracking(k+1, i)

backtracking(0, 0)
def backtracking(nums, arr, n, m):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    
    for num in nums:
        if len(arr) != 0:
            if num >= arr[-1]:
                arr.append(num)
                backtracking(nums, arr, n, m)
                arr.pop()
        else:
            arr.append(num)
            backtracking(nums, arr, n, m)
            arr.pop()
        
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = []

backtracking(nums, arr, N, M)
N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

arr = [0 for _ in range(M)]

def backtracking(k, start):
    if k == M:
        print(' '.join(map(str, arr)))
        return

    tmp = 0
    for i in range(start, N):
        if(tmp != nums[i]):
            arr[k] = nums[i]
            tmp = arr[k]
            backtracking(k+1, i+1)

backtracking(0, 0)
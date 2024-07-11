N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

isused = [False for _ in range(N)]
arr = [0 for _ in range(M)]

def backtracking(k):
    if k == M:
        print(' '.join(map(str, arr)))
        return

    
    tmp = 0
    for i in range(N):
        
        if(isused[i] == False and tmp != nums[i]):
            isused[i] = True
            arr[k] = nums[i]
            tmp = arr[k]

            backtracking(k+1)

            isused[i] = False

backtracking(0)
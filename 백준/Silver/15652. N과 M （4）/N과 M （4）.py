def backtracking(arr, n, m):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, N+1):
        if len(arr) != 0:
            if i >= arr[-1]:
                arr.append(i)
                backtracking(arr, n, m)
                arr.pop()
        else:
                arr.append(i)
                backtracking(arr, n, m)
                arr.pop()
        
N, M = input().split()
N = int(N)
M = int(M)
arr = []

backtracking(arr, N, M)
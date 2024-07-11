def backtraking(arr, n, m):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, n+1):
        arr.append(i)
        backtraking(arr, n, m)
        arr.pop()

N, M = input().split()

N = int(N)
M = int(M)
arr = []

backtraking(arr, N, M)
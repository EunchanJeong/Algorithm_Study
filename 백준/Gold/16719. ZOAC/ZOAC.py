import sys
input = sys.stdin.readline

arr = list(input().strip())
result = [''] * len(arr)

def dfs(index, arr):
    if not arr:
        return

    c = min(arr)
    idx = arr.index(c)

    result[index + idx] = c
    print(''.join(result))

    dfs(index+idx+1, arr[idx+1:])
    dfs(index, arr[:idx])

dfs(0, arr)
def solution(arr, n):
    if len(arr)%2 == 0:
        for i, val in enumerate(arr):
            if i % 2 != 0:
                arr[i] = val+n
    else:
        for i, val in enumerate(arr):
            if i % 2 == 0:
                arr[i] = val+n
    return arr
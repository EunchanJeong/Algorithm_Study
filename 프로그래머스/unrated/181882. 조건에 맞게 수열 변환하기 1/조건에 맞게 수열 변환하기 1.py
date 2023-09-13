def solution(arr):
    for i, val in enumerate(arr):
        if val >= 50 and val%2 == 0:
            arr[i] = val/2
        elif val < 50 and val%2 != 0:
            arr[i] = val*2
    return arr
def solution(arr, idx):
    
    tmp = arr[idx:]
    
    if 1 in tmp:
        return idx+tmp.index(1)
    else:
        return -1
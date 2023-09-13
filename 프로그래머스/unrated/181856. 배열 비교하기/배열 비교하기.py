def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        if len(arr2)>len(arr1):
            return -1
        elif len(arr2)<len(arr1):
            return 1
    else: 
        if sum(arr2)>sum(arr1):
            return -1
        elif sum(arr2)<sum(arr1):
            return 1
    return 0
        
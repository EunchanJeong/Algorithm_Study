def solution(arr, delete_list):
    
    for num in delete_list:
        if num in arr:
            idx = arr.index(num)
            arr.pop(idx)
    return arr
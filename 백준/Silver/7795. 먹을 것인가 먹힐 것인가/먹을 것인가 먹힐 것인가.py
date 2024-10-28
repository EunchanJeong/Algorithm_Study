def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left

N = int(input())

for _ in range(N):
    len_A, len_B = map(int, input().split())
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    
    count = 0
    
    for a in A:
        count += binary_search(B, a)
    
    print(count)
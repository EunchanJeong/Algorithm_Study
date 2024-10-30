import sys

N = int(input())
A = list(map(int, input().split()))
A.sort()

left, right = 0, N-1
num_max = sys.maxsize
result = [A[left], A[right]]

while left < right:
    num_sum = A[left] + A[right]
    if abs(num_sum) < num_max:
        num_max = abs(num_sum)
        result[0] = A[left]
        result[1] = A[right]
        
    if num_sum > 0:
        right -= 1
    elif num_sum < 0:
        left += 1
    else:
        break
print(result[0], result[1])
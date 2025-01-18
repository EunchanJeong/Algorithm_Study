import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))

L.sort()

left = 0
right = N-1
min_value = float('inf')

result  = [L[left], L[right]]
while left < right:
    value = L[left] + L[right]

    if abs(value) < min_value:
        min_value = abs(value)
        result = [L[left], L[right]]

    if value < 0:
        left += 1
    elif value > 0:
        right -= 1
    else:
        break

print(result[0], result[1])

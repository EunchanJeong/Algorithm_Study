import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))

left, right = 0, N-1
result = L[left] + L[right]

while left < right:
    tmp = L[left] + L[right]

    if abs(result) > abs(tmp):
        result = tmp

    if tmp < 0:
        left += 1
    else:
        right -= 1

print(result)
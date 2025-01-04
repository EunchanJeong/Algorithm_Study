n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
S = sum(A[i] * b for i, b in enumerate(sorted(B, reverse=True)))

print(S)
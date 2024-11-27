import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

count = 0
for a in A:
    a -= B
    count += 1
    if a <= 0:
        continue
    else:
        count += a//C
        a = a%C

        if a > 0:
            count += 1

print(count)
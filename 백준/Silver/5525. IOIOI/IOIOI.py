import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

P = 'IO'* N + 'I'

count = 0
for i in range(M-len(P)+1):
    if S[i] == 'I':
        if S[i:i+len(P)] == P:
            count += 1

print(count)
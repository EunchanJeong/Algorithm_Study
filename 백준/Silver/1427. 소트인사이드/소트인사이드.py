import sys
input = sys.stdin.readline

N = list(input())
N.sort(reverse=True)

print(''.join(N))
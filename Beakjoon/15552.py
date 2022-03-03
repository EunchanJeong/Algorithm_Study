import sys

size = int(input())

for i in range(size):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

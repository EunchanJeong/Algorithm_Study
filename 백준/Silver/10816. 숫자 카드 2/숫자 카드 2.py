import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
counts = list(map(int, input().split()))


num_dic = {}

for c in cards:
    if c in num_dic:
        num_dic[c] += 1
    else:
        num_dic[c] = 1

for c in counts:
    if c in num_dic:
        print(num_dic[c], end=' ')
    else:
        print(0, end=' ')
import sys
input = sys.stdin.readline

N = int(input())

dic = {}
for _ in range(N):
    name, extension = input().strip().split('.')

    if extension not in dic:
        dic[extension] = 1
    else:
        dic[extension] += 1

dic = sorted(dic.items())

for extension, count in dic:
    print(extension, count)
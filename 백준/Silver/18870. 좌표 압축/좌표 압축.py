import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

set_X = list(set(X))
set_X.sort()

dic = {}
for i in range(len(set_X)):
    dic[set_X[i]] = i

for x in X:
    print(dic[x], end=' ')
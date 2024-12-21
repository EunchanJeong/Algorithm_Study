import sys
input = sys.stdin.readline

def check(a, b, op):
    if op == '<':
        if a > b:
            return False
    if op == '>':
        if a < b:
            return False
    return True

def dfs(count, num):
    if count == k+1:
        result.append(num)
        return

    for i in range(10):
        if visited[i] == 0:
            if count == 0 or check(num[count-1], str(i), L[count-1]):
                visited[i] = 1
                dfs(count + 1, num + str(i))
                visited[i] = 0


k = int(input())
L = list(map(str, input().split()))

visited = [0] * 10
result = []

dfs(0, '')
result.sort()

print(result[-1])
print(result[0])
import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

stack = []
result = 0

for s in S:
    if len(stack) == 0 or stack[-1] == s:
        stack.append(s)
    else:
        if len(stack) != 0:
            stack.pop()

    result = max(result, len(stack))

if len(stack) == 0:
    print(result)
else:
    print(-1)
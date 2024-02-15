import sys

N = int(sys.stdin.readline())
top_list = list(map(int, sys.stdin.readline().split()))
stack = []
output = []

for i in range(N):
    while stack:
        if stack[-1][1] > top_list[i]:
            output.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        output.append(0)
    stack.append([i, top_list[i]])

print(" ".join(map(str, output)))
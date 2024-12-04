import sys
input = sys.stdin.readline

N = int(input())
buildings = []
for _ in range(N):
    buildings.append(int(input()))

stack = []
count = 0

for i in range(N):
    while stack and stack[-1] <= buildings[i]:
        stack.pop()
    count += len(stack)

    stack.append(buildings[i])

print(count)
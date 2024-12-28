import sys
input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    op = input().strip()

    max_depth = 0
    stack = []
    for char in op:
        if char == ']':
            max_depth = max(len(stack), max_depth)
            stack.pop()
        else:
            stack.append('[')

    print(2 ** max_depth)
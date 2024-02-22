import sys
input = sys.stdin.readline

N = int(input())
good_count = 0

for _ in range(N):
    text = input().rstrip()
    stack = []

    for t in text:
        if stack:
            if t == stack[-1]:
                stack.pop()
            else:
                stack.append(t)
        else:
            stack.append(t)
        
    if not stack:
        good_count += 1

print(good_count)
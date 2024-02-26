import sys
input = sys.stdin.readline

inputs = input()

stack = []
count = 0
lazer = 0

for i in inputs:
    if i == ')':
        stack.pop()
        if lazer == 1:
            count+= len(stack)
            lazer = 0
        else:
            count += 1
    else:
        stack.append(i)
        lazer = 1

print(count)
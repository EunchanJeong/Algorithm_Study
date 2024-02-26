import sys
input = sys.stdin.readline

text = input().rstrip()

tmp = 1
stack = []
result = 0

for i, t in enumerate(text):
    
    if t == '(':
        stack.append(t)
        tmp *= 2
    elif t == '[':
        stack.append(t)
        tmp *= 3

    elif t == ')':

        if not stack:
            result = 0
            break

        k = stack.pop()

        if k == '[':
            result = 0
            break
        if text[i-1] == '(':
            result += tmp
        tmp //= 2

    elif t == ']':
        if not stack:
            result = 0
            break

        k = stack.pop()

        if k == '(':
            result = 0
            break
        if text[i-1] == '[':
            result += tmp
        tmp //= 3

if stack:
    print(0)
else:
    print(result)
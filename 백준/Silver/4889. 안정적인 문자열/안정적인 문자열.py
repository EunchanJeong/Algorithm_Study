import sys
input = sys.stdin.readline

result = []
while True:
    S = input().strip()

    if '-' in S:
        break

    stack = []
    count = 0
    for s in S:
        if s == '{':
            stack.append(s)
        elif s == '}':
            if len(stack) == 0:
                count += 1
                stack.append('{')
            else:
                stack.pop()

    if len(stack) != 0:
        count += len(stack)//2

    result.append(count)

for i in range(1, len(result)+1):
    print(f'{i}. {result[i-1]}')
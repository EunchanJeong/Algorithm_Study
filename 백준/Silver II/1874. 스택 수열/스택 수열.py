import sys

tmp = True
count = 1
stack = []
op = []

N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())

    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        tmp = False
        break

if tmp == False:
    print('NO')
else:
    for i in op:
        print(i)
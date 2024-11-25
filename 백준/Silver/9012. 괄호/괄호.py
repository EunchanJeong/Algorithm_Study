import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    s = []

    tmp = list(input())

    check = True
    for t in tmp:
        if t == '(':
            s.append(t)
        elif t == ')':
            if len(s) != 0:
                s.pop()
            else:
                print('NO')
                check = False
                break
    if check:
        if len(s) == 0:
            print('YES')
        else:
            print('NO')
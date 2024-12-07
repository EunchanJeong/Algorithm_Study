import sys
input = sys.stdin.readline

S = input().strip()

result = ''
tmp = ''
for s in S:
    if s == '>':
        result += tmp + s
        tmp = ''

    elif s == '<':
        if len(tmp) == 0:
            tmp += s
        else:
            result += tmp[::-1]
            tmp = '<'
    elif s == ' ':
        if '<' in tmp:
            tmp += s
        else:
            result += tmp[::-1] + s
            tmp = ''
    else:
        tmp += s

if len(tmp) != 0:
    result += tmp[::-1]
print(result)
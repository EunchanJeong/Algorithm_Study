import sys
input = sys.stdin.readline

S = list(input().strip())

zero_count = S.count('0')
one_count = S.count('1')

stop_point = 0
for w in S:
    if w == '1':
        S.remove(w)
        stop_point += 1

    if stop_point == one_count//2:
        break

S = S[::-1]
stop_point = 0
for w in S:
    if w == '0':
        S.remove(w)
        stop_point += 1

    if stop_point == zero_count // 2:
        break

print(''.join(S[::-1]))

len_A, len_B = map(int, input().split())
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

d = list(A-B)

if len(d) == 0:
    print(0)
else:
    print(len(d))
    d.sort()
    for i in d:
        print(i, end=' ')
N = int(input())

arr = []
for _ in range(N):
    tmp = input()
    
    num = ''
    for a in tmp:
        if a.isdigit():
            num += a
        else:
            if num != '':
                arr.append(int(num))
                num = ''
    if num.isdigit():
        arr.append(int(num))
arr.sort()

for a in arr:
    print(a)     
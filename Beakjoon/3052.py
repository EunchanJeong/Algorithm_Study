r = []

count = 0

for i in range(10):
    n = int(input())%42
    if n not in r:
        r.append(n)
        count += 1

print(count)
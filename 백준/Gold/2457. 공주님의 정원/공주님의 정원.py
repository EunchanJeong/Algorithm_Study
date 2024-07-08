N = int(input())

flowers = []

for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    start = sm * 100 + sd
    end = em * 100 + ed
    flowers.append((start, end))

flowers.sort()

t = 301
f_count = 0
idx = 0
max_end = 0

while t <= 1130:
    updated = False
    while idx < N and flowers[idx][0] <= t:
        if flowers[idx][1] > max_end:
            max_end = flowers[idx][1]
            updated = True
        idx += 1
    
    if not updated:
        print(0)
        exit()
    
    f_count += 1
    t = max_end

print(f_count)
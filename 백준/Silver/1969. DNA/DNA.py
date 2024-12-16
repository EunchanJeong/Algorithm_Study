n, m = map(int, input().split())
data = [input() for _ in range(n)]

result = ''
count = 0
for i in range(m):
    dna = ['A', 'C', 'G', 'T']
    cnt = [0, 0, 0, 0]
    for d in data:
        cnt[dna.index(d[i])] += 1

    index = cnt.index(max(cnt))
    result += dna[index]
    count += sum(cnt) - max(cnt)

print(result)
print(count)
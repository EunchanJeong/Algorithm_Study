size = int(input())
r = []

for i in range(size):
    scores = list(map(int, input().split()))
    m = sum(scores[1:]) / scores[0]
    count = 0

    for j in scores[1:]:
        if (j > m):
            count += 1

    r.append((count/scores[0]) * 100)

for i in range(len(r)):
    print("{:.3f}%".format(r[i]))

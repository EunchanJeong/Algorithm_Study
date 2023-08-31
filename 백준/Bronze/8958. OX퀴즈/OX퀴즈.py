size = int(input())
result = []

for i in range(size):
    q = input()
    tmp = []
    count = 0
    score = 0

    for j in range(len(q)):
        if q[j] == "O":
            count += 1
            score += count
        else:
            tmp.append(score)
            count = 0
            score = 0

    tmp.append(score)
    result.append(sum(tmp))

for i in range(size):
    print(result[i])
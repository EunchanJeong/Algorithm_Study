T = int(input())

changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]


for t in range(1, T+1):
    m = int(input())
    answer = []

    for c in changes:
        count = 0
        while m >= c:
            m -= c
            count += 1
        answer.append(str(count))
    print(f"#{t}")
    print(f"{' '.join(answer)}")
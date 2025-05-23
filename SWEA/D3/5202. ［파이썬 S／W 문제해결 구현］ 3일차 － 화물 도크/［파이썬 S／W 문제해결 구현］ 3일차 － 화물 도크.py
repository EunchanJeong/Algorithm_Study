T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    times = []
    for _ in range(N):
        times.append(list(map(int, input().split())))
    times.sort(key=lambda x : [-x[1], -x[0]])

    start, end = times.pop()
    count = 1

    while times:
        next_s, next_e = times.pop()
        if end <= next_s:
            start, end = next_s, next_e
            count += 1

    print(f"#{test_case} {count}")
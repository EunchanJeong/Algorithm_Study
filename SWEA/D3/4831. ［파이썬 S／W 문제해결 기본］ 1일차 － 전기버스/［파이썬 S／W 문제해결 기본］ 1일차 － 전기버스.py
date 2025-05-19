T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))

    now = 0
    go = now + K
    charge_station = 0
    count = 0

    while (go < N):
        for s in stations:
            if now < s <= go:
                charge_station = s
            elif go < s:
                break

        if charge_station == -1:
            count = 0
            break

        now = charge_station
        count += 1
        go = now + K
        charge_station = -1

    print(f"#{test_case} {count}")
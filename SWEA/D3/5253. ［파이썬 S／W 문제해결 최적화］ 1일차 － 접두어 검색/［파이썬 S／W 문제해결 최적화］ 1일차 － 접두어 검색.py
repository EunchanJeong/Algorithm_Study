T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    A = []
    B = []

    for _ in range(N):
        A.append(input())
    for _ in range(M):
        B.append(input())

    count = 0
    index = set()
    for a in A:
        for b in B:
            if a[0:len(b)] == b:
                index.add(b)
    print(f"#{test_case} {len(index)}")
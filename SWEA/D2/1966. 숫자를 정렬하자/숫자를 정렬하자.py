T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    print(f"#{test_case} {' '.join(map(str, L))}")
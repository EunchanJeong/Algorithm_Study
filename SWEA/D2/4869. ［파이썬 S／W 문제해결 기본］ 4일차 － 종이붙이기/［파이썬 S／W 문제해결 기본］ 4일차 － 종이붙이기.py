def count(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return count(n-1) + count(n-2) * 2

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    num = count(N//10)
    print(f"#{test_case} {num}")
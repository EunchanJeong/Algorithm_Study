from collections import Counter

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(input())
    count = Counter(nums)

    sorted_items = sorted(count.items(), key=lambda x: (-x[1], -int(x[0])))

    print(f"#{test_case} {sorted_items[0][0]} {sorted_items[0][1]}")

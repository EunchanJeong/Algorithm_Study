import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    W = input().strip()
    K = int(input())
    char_idx = {}

    for i, char in enumerate(W):
        if char not in char_idx:
            char_idx[char] = []

        char_idx[char].append(i)

    min_len = float('inf')
    max_len = -1

    for idx_list in char_idx.values():
        if len(idx_list) < K:
            continue

        for i in range(len(idx_list) - K + 1):
            length = idx_list[i + K - 1] - idx_list[i] + 1

            min_len = min(min_len, length)
            max_len = max(max_len, length)

    if min_len == float('inf'):
        print(-1)
    else:
        print(min_len, max_len)
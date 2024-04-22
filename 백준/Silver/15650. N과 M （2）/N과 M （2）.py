n, m = map(int, input().split())
nn = []


def backtracking(k):
    if len(nn) == m:
        print(' '.join(map(str, nn)))
    for i in range(k, n + 1):
        if i not in nn:
            nn.append(i)
            backtracking(i)
            nn.pop()


backtracking(1)
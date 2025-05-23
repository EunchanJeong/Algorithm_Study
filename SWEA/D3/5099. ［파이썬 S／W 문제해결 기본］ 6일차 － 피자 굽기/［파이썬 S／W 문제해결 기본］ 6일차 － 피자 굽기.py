from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    pizzas = list(map(int, input().split()))

    q = deque()
    for idx, value in enumerate(pizzas[0:N]):
        q.append((idx, value))

    new_idx = N

    while len(q) > 1:
        idx, pizza = q.popleft()

        pizza //= 2

        if pizza > 0:
            q.append((idx, pizza))

        if len(q) < N and new_idx < len(pizzas):
            q.append((new_idx, pizzas[new_idx]))
            new_idx += 1

    result, pizza = q.popleft()

    print(f"#{test_case} {result+1}")
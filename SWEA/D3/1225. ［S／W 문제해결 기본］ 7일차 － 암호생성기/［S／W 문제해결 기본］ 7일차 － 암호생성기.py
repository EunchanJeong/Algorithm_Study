from collections import deque

for _ in range(10):
    test_case = int(input())
    q = deque(list(map(int, input().split())))

    count = 1
    while True:
        if count == 6:
            count = 1

        front = q.popleft()

        if front - count <= 0:
            q.append(0)
            break

        q.append(front - count)
        count += 1

    print(f"#{test_case} ", end="")
    for n in q:
        print(f"{n} ", end="")
    print()
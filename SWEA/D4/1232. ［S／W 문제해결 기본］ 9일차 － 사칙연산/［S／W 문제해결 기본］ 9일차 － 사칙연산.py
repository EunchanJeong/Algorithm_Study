for test_case in range(1, 11):
    N = int(input())

    tmp = []
    for _ in range(N):
        tmp.append(list(input().split()))

    inputs = [0] * (N+1)

    tmp.reverse()

    for t in tmp:
        if len(t) == 2:
            inputs[int(t[0])] = int(t[1])
        else:
            if t[1] == "+":
                inputs[int(t[0])] = inputs[int(t[2])] + inputs[int(t[3])]
            elif t[1] == "-":
                inputs[int(t[0])] = inputs[int(t[2])] - inputs[int(t[3])]
            elif t[1] == "*":
                inputs[int(t[0])] = inputs[int(t[2])] * inputs[int(t[3])]
            elif t[1] == "/":
                inputs[int(t[0])] = inputs[int(t[2])] // inputs[int(t[3])]

    print(f"#{test_case} {inputs[1]}")
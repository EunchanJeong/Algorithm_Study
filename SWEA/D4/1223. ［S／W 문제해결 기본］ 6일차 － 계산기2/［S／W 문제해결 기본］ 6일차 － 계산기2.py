for test_case in range(1, 11):
    N = int(input())
    s = list(input())

    nums = []
    while len(s) > 0:
        t = s.pop()

        if t.isdigit():
            nums.append(int(t))
        elif t == "*":
            num1 = nums.pop()
            t = int(s.pop())

            nums.append(num1 * t)

    print(f"#{test_case} {sum(nums)}")
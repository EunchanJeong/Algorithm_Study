for test_case in range(1, 11):
    N = int(input())

    inputs = list(input())

    stack = []
    result = 1

    for i in inputs:
        if i == ")":
            if stack[-1] != "(":
                result = 0
                break
            stack.pop()
        elif i == "]":
            if stack[-1] != "[":
                result = 0
                break
            stack.pop()
        elif i == "}":
            if stack[-1] != "{":
                result = 0
                break
            stack.pop()
        elif i == ">":
            if stack[-1] != "<":
                result = 0
                break
            stack.pop()
        else:
            stack.append(i)

    print(f"#{test_case} {result}")
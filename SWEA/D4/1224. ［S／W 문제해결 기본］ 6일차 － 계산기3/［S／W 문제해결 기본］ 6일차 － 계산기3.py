for test_case in range(1, 11):
    N = int(input())
    s = list(input())
    stack = []
    result = ""

    for t in s:
        if t.isdigit():
            result += t
        else:
            if t == "(":
                stack.append(t)
            elif t == "*":
                while stack and stack[-1] == "*":
                    result += stack.pop()
                stack.append(t)
            elif t == "+":
                while stack and stack[-1] != "(":
                    result += stack.pop()
                stack.append(t)
            elif t == ")":
                while stack and stack[-1] != "(":
                    result += stack.pop()
                stack.pop()
    while stack:
        result += stack.pop()

    stack = []
    for i in result:
        if i == "+":
            stack.append(stack.pop() + stack.pop())
        elif i == "*":
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(i))
    print(f"#{test_case} {stack.pop()}")
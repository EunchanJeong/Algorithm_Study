text = '1'

while True:
    text = input()

    if text == '.':
        break

    error = 0
    stack = []

    for t in text:
        if t == '(' or t == '[':
            stack.append(t)
        elif t == ')' or t == ']':
            if len(stack) == 0:
                print('no')
                error = 1
                break
            else:
                k = stack.pop()

            if k == '(' and t != ')':
                print('no')
                error = 1
                break
            elif k == '[' and t != ']':
                print('no')
                error = 1
                break
    
    if error == 0:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')
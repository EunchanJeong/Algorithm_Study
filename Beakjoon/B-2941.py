s = input()

change = []

for i in s:
    change.append(i)

    index = len(change) - 1

    if change[index] == '=':
        if change[index - 1] == 'z':
            if change[index - 2] == 'd':
                change[index - 2:] = '*'
            else:
                change[index - 1:] = '*'

        else:
            change[index - 1:] = '*'
    elif change[index] == '-':
        change[index - 1:] = '*'
    elif change[index] == 'j':
        if change[index - 1] == 'l' or change[index - 1] == 'n':
            change[index - 1:] = '*'

print(len(change))
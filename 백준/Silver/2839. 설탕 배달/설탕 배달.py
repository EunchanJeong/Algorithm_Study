a = int(input())
count = 0

if a == 4 or a == 7:
    print("-1")
else:
    if a % 5 == 0:
        count = a // 5
    elif a % 5 == 1:
        count = ((a - (3 * 2)) // 5) + 2
    elif a % 5 == 2:
        count = ((a - (3 * 4)) // 5) + 4
    elif a % 5 == 3:
        count = (a - 3 * 1) // 5 + 1
    elif a % 5 == 4:
        count = ((a - 3 * 3) // 5) + 3
    print(count)
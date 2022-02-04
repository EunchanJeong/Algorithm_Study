size = int(input())

for i in range(size, 0, -1):
    for j in range(i-1):
        print(" ", end='')
    for k in range(size-i+1):
        print("*", end='')
    print()
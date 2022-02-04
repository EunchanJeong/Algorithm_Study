max_num = 0
index = 0

for i in range(9):
    num = int(input())

    if max_num < num:
        max_num = num
        index = (i + 1)

print(max_num)
print(index)
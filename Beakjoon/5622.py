ASCII = 65
count = 0
num = 2
dial = {}

for i in range(65, 91, 1):
    dial[chr(i)] = num+1
    count += 1

    if num == 7 or num == 9:
        if count == 4:
            count = 0
            num += 1
    else:
        if count == 3:
            num += 1
            count = 0


word = input()

second = 0

for i in word:
    second += dial[i]

print(second)
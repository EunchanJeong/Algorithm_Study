import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    word = input().strip()

    if word == word[::-1]:
        print(0)
    else:
        check = False
        front, back = 0, len(word)-1
        for _ in range(len(word)):
            if front >= back:
                break
            if word[front] == word[back]:
                front += 1
                back -= 1
                continue

            if word[front] == word[back-1]:
                tmp = word[front:back]
                if tmp == tmp[::-1]:
                    check = True
                    break

            if word[front+1] == word[back]:
                tmp = word[front+1:back+1]
                if tmp == tmp[::-1]:
                    check = True
                    break
            break
        if check:
            print(1)
        else:
            print(2)
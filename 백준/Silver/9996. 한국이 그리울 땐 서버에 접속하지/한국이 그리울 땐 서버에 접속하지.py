N = int(input())
T = list(map(str, input().split('*')))

answer = []
for _ in range(N):
    word = input()
    s = word[0:len(T[0])]

    word = word[len(T[0])-1:]
    e = word[-(len(T[1])):]
    if s == T[0] and e == T[1]:
        answer.append('DA')
    else:
        answer.append('NE')

for a in answer:
    print(a)
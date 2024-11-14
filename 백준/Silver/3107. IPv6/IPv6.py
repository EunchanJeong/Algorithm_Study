N = input()
L = list(N.split(':'))
zero = ['0000'] * (8 - (len(L) - L.count('')))
zero = ':'.join(map(str, zero))

count = 0
answer = ''
for i in range(len(L)):
    t = '0' * (4 - len(L[i]))
    if i == 0:
        if L[i] == '':
            if count == 0:
                answer += zero
                count += 1
        else:

            answer += (t + L[i])
    else:
        if L[i] == '':
            if count == 0:
                answer += ':' + zero
                count += 1
        else:
            answer += ':' + t+ L[i]
print(answer)
N,M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

answer = []

a = 0
b = 0
while a != len(A) or b != len(B):

    if a == len(A):
        answer.append(B[b])
        b+=1
    elif b == len(B):
        answer.append(A[a])
        a+=1
    else:
        if A[a]<B[b]:
            answer.append(A[a])
            a+=1
        else:
            answer.append(B[b])
            b+=1


print(' '.join(map(str, answer)))
import sys

input = sys.stdin.readline

def check(S):
    global result

    if len(S) == 1:
        result = 'AKARAKA'
    else:

        if S == S[::-1]:
            N = len(S)//2
            check(S[:N])
            check(S[-N:])
        else:
            return


S = input().strip()
result = "IPSELENTI"

check(S)
print(result)
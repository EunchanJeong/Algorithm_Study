import sys
input = sys.stdin.readline

S, E = map(int, input().split())

def is_prime_num(S, E):
    arr = [True] * (E + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, E + 1):
        if arr[i] == True:
            j = 2

            while (i * j) <= E:
                arr[i*j] = False
                j += 1
    return arr

arr = is_prime_num(S, E)
for i in range(S, E+1):
    if arr[i]:
        print(i)
    
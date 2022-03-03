A = int(input())
B = int(input())
C = int(input())

N = A * B * C

str_N = str(N)

num = [0 for _ in range(10)]

for i in range(len(str_N)):
    num[int(str_N[i])] += 1

for i in range(10):
    print(num[i])
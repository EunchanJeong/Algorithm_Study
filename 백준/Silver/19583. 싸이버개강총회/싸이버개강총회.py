import sys
input = sys.stdin.readline

S, E, Q = input().strip().split()

S = int(S[:2] + S[3:])
E = int(E[:2] + E[3:])
Q = int(Q[:2] + Q[3:])

A = set()
count = 0

while True:
    try:
        time, name = input().split()
        time = int(time[:2] + time[3:])

        if time <= S:
            A.add(name)
        elif E <= time <= Q and name in A:
            A.remove(name)
            count += 1
    except:
        break
print(count)
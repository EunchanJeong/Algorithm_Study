T = int(input())

for t in range(1, T+1):
    L = list(map(int, input().split()))
    L.sort()
    L = L[1:len(L)-1]
   
    avg = sum(L)/len(L)
    print(f'#{t} {round(avg)}')
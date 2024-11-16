T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    if N > M:
        tmp = arr1
        arr1 = arr2
        arr2 = tmp

    size = len(arr2) - len(arr1)
    answer = 0
    for i in range(size+1):
        tmp = arr2[i:i+len(arr1)]
        p = sum([arr1[i] * tmp[i] for i in range(len(arr1))])
    
        if p > answer:
            answer = p

    print(f'#{t} {answer}')
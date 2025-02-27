t = int(input())

for i in range(t):
    n = int(input())
    case = list(map(int, input().split()))
    case.sort()
    
    arr1 = []
    arr2 = []
    for j in range(0, n, 2):
        arr1.append(case[j])
    for j in range(1, n, 2):
        arr2.append(case[j])
    arr2.sort(reverse = True)
    arr1 += arr2
    answer = abs(arr1[-1] - arr1[0])
    
    for j in range(n - 1):
        sub = abs(arr1[j] - arr1[j + 1])
        if sub > answer:
            answer = sub

    print(answer)
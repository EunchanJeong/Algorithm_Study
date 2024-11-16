T = int(input())

nums = [2, 3, 5, 7, 11]
for test_case in range(1, T+1):
    N = int(input())
    
    answer = []
    for i in nums:
        count = 0
        
        while N%i == 0:
            N = N//i
            count += 1
        answer.append(count)
    print(f"#{test_case} {' '.join(map(str, answer))}")
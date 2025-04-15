for _ in range(10):
    test_case = int(input())

    nums = []
    for _ in range(100):
        nums.append(list(map(int, input().split())))


    diagonal_sum = 0
    rediagonal_sum = 0
    answer = 0
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += nums[i][j]
            col_sum += nums[j][i]
        
        answer = max(answer, row_sum, col_sum)
        
        diagonal_sum += nums[i][i]
        rediagonal_sum += nums[i][100 - i - 1]

    answer = max(answer, diagonal_sum, rediagonal_sum)
    print(f'#{test_case} {answer}')
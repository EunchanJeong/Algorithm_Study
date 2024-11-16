days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
T = int(input())
for test_case in range(1, T + 1):
    month1, day1, month2, day2 = map(int, input().split())

    answer = 0
    if month1 - month2 != 0:
        for m in range(month1 + 1, month2, 1):
            answer += days[m]
        answer += days[month1] - day1 + 1
        answer += day2
    else:
        answer = day2 - day1 + 1

    print(f'#{test_case} {answer}')
T = int(input())

for test_case in range(1, T+1):
    text = input()
    answer = 0
    for i in range(1, len(text)//2 + 1):
        if text[0:i] == text[i:i * 2]:
            answer = len(text[0:i])
            break

    print(f'#{test_case} {answer}')
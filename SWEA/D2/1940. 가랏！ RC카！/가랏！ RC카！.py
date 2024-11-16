T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    d = 0
    speed = 0
    for i in range(N):
        command = list(map(int, input().split()))

        if len(command) == 1:
            d += speed
        else:
            if command[0] == 1:
                speed += command[1]
                d += speed

            else:
                speed -= command[1]
                if speed < 0:
                    speed = 0
                d += speed
                
    print(f'#{test_case} {d}')
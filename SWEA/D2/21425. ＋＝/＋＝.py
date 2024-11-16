T = int(input())

for test_case in range(1, T+1):
    x, y, N = map(int, input().split())
    
    count = 0
    while True:
        if x > y:
            y += x
        else:
            x += y
        count += 1
        if x > N or y > N:
            break
    print(f'{count}')
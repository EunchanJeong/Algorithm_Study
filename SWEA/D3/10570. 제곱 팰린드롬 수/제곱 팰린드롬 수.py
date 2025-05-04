T = int(input())

for test_case in range(1, T + 1):
    start, end = map(int, input().split())
    count = 0
    for i in range(start, end+1):
        if str(i) == str(i)[::-1]:
            q = i ** (1/2)
            
            if float(q).is_integer() and str(int(q)) == str(int(q))[::-1]:
                count += 1
    
    print(f"#{test_case} {count}")
T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    
    alphabets = {}
    for s in str1:
        alphabets[s] = 0
    
    for s in str2:
        if s in alphabets:
            alphabets[s] += 1
    
    tmp = [v for k,v in alphabets.items() if max(alphabets.values()) == v]
    
    print(f'#{test_case} {tmp[0]}')
T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    b1 = []
    for i in range(A):
        b1.append(input())
    
    count = 0
    for i in range(B):
        book = input()
        
        if book in b1:
            count += 1
    
    print(f"#{test_case} {count}")

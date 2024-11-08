T = int(input())

for i in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    sell_price = 0
    answer = 0
    for n in nums[::-1]:
        if n >= sell_price:
            sell_price = n
        else:
            answer += (sell_price - n)
    print("#" + str(i+1) + " " + str(answer))
        
    
                
                
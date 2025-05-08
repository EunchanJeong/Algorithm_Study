T = int(input())

for test_case in range(1, T + 1):
    word = list(input())
    
    check = True
    while True:
        if not check:
        	break
        
        check = False
        pre = word[0]
        for idx, w in enumerate(word[1:]):
            if pre == w:
                word.pop(idx)
                word.pop(idx)

                check = True
                break
            pre = w

    print(f"#{test_case} {len(word)}")
                
            
       
        
        
    
    

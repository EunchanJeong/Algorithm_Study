for i in range(1, 11):
    N = int(input())
    apts = list(map(int, input().split()))
    count = 0
    for j in range(2, len(apts)-2):
        f = max(apts[j-2:j])
        b = max(apts[j+1:j+3])
        n = max(f, b)
        
       	p = apts[j] - n
        
        if p > 0:
            count += p
    print('#' + str(i) + ' ' + str(count))
       
        
        
  
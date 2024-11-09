N = int(input())

for i in range(1, N+1):
    list_i = list(str(i))
    
    sum = list_i.count('3') + list_i.count('6') + list_i.count('9')
    
    if sum == 0:
        print(i, end = ' ')
    else:
        print('-'*sum, end = ' ')
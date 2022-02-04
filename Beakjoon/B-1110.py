num = int(input())

count = 0
result = num

while (True):
    left = result // 10   # 수의 왼쪽값
    right = result % 10   # 수의 오른쪽값

    sum = left + right   # 왼쪽과 오른쪽을 더한다.

    result = (right*10) + (sum%10)   # 수의 오른쪽값은 십의 자리수, 더한값의 오른쪽값은 일의 자리수
     
    count += 1
    
    if result == num:
        print(count)
        print(count)
        break
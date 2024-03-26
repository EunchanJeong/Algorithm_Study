def solution(my_string, num1, num2):
    if num1 > num2:
        tmp = num1
        num2 = num1
        num1 = tmp
    answer = my_string[:num1] + my_string[num2] + my_string[num1+1:num2] + my_string[num1] + my_string[num2+1:]
    return answer
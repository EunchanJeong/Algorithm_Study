def solution(my_string):
    my_string = list(my_string)
    print(my_string)
    my_string = my_string[::-1]
    answer = ''.join(my_string)
    return answer
def solution(my_string, letter):
    my_string = list(my_string)
    while True:
        if letter in my_string:
            my_string.pop(my_string.index(letter))
        else:
            break
    answer = ''.join(my_string)
    return answer
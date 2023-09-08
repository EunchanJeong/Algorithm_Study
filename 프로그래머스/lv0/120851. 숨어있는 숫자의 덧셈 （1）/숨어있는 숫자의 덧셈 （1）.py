def solution(my_string):
    answer = 0
    for string in my_string:
        if str.isdigit(string):
            answer += int(string)

    return answer
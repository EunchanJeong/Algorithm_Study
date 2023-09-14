def solution(my_string):
    my_string = list(my_string)
    for i, val in enumerate(my_string):
        if val.isupper():
            my_string[i] = val.lower()
        else:
            my_string[i] = val.upper()
    return ''.join(my_string)
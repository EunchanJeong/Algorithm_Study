def solution(my_strings, parts):
    for i, val in enumerate(my_strings):
        my_strings[i] = val[parts[i][0]:parts[i][1]+1]
    return ''.join(my_strings)
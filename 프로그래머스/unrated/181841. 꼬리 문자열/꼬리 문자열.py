def solution(str_list, ex):
    for i, val in enumerate(str_list):
        if ex in val:
            str_list[i] = ''
        
    return ''.join(str_list)
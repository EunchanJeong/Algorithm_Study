def solution(n_str):
    n_str = list(n_str)
    
    for i, val in enumerate(n_str):
        if val == '0':
            n_str[i] = ''
        else:
            break
    return ''.join(n_str)
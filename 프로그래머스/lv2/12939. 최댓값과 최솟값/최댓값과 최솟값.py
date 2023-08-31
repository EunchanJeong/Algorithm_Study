def solution(s):
    s = s.split()
    s = list(map(int, s))
    answer = f'{min(s)} {max(s)}'
    return answer
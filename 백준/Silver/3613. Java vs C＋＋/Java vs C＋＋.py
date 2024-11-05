def check(word):
    w_cnt = 0
    u_cnt = 0

    if word[0] == '_' or word[0].isupper() or word[-1] == '_':
        return 'Error!'

    for i, t in enumerate(target):
        if t.isupper():
            w_cnt += 1

        elif t == '_':
            u_cnt += 1
            if target[i-1] == '_':
                return 'Error!'
    if w_cnt > 0 and u_cnt > 0:
        return 'Error!'
    elif w_cnt > 0:
        return 'Java'
    elif u_cnt > 0:
        return 'C++'
    else:
        return word

def java_to_c(s):
    cv = ''
    for c in s:
        if ord('A') <= ord(c) and ord(c) <= ord('Z'):
            cv += '_'
            cv += c.lower()
        else:
            cv += c

    return cv

def c_to_java(s):
    cv = ''
    upper_flg = False
    for c in s:
        if c == '_':
            upper_flg = True
        else:
            if upper_flg:
                cv += c.upper()
                upper_flg = False
            else:
                cv += c

    return cv

target = input().strip('\n')
mode = check(target)
if mode == 'Error!':
    print(mode)
elif mode == 'Java':
    print(java_to_c(target))
elif mode == 'C++':
    print(c_to_java(target))
else:
    print(mode)
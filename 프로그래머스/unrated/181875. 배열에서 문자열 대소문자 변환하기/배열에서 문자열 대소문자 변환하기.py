def solution(strArr):
    count = 0
    
    for i, val in enumerate(strArr):
        if i%2 == 0:
            strArr[i] = val.lower()
            count = 1
        else:
            strArr[i] = val.upper()

    return strArr
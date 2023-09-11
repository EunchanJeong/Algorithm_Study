def solution(strArr):
    count = 0
    
    for i, val in enumerate(strArr):
        if count == 0:
            strArr[i] = val.lower()
            count += 1
        else:
            strArr[i] = val.upper()
            count -= 1
    return strArr
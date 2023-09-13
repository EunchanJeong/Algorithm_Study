def solution(myString, pat):
    myString = list(myString)
    
    for i, val in enumerate(myString):
        if val == 'A':
            myString[i] = 'B'
        else:
            myString[i] = 'A'
    
    if pat in ''.join(myString):
        return 1
    else:
        return 0

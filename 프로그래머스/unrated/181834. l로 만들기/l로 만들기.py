def solution(myString):
    
    alpabets = list(myString)
    alpabets = list(set(alpabets))
    alpabets = [x for x in alpabets if x < 'l']

    for alpabet in alpabets:
        myString = myString.replace(alpabet, 'l')
    return myString
def cal(x):
    x = x.split()
    
    if x[1] == '+':
        if (int(x[0]) + int(x[2])) == int(x[4]):
            return "O"
        else:
            return "X"
    elif x[1] == '-':
        if (int(x[0]) - int(x[2])) == int(x[4]):
            return "O"
        else:
            return "X"
def solution(quiz):
    answer = []
    for i in quiz:
        answer.append(cal(i))
    return answer
def solution(num, k):
    num = str(num)

    if num.find(str(k)) != -1:
        print(num.find(str(k)))
        return num.find(str(k))+1
    return -1
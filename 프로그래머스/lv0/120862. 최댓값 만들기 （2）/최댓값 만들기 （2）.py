def solution(numbers):
    answer = numbers[0]*numbers[1]
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            tmp = numbers[i]*numbers[j]
            if answer < tmp:
                answer = tmp
    return answer
def solution(numbers):
    answer = 0
    
    for i in range(len(numbers)):
        for j in  range(i+1, len(numbers)):
            result = numbers[i]*numbers[j]
            if result > answer:
                answer = result
    return answer
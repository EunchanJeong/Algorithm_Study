def solution(n):
    answer = n
    
    for i in range(1, n):
        if n % i == 1:
            print(i)
            if i < answer:
                answer = i

    return answer
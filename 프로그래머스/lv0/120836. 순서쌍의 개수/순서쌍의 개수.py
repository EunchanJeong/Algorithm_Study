def solution(n):
#     a = n//2
                    
#     answer = 0
#     limit = a
    
#     for i in range(1, a+1):
#         for j in range(1, limit+1):
#             if i * j == n:
#                 answer += 1
#                 limit = j
#                 break
#     answer += 2
    
#     if n == 1:
#         answer = 1
    
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += 1

    return answer
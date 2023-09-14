def solution(cipher, code):

    answer = cipher[(code-1)::code]
    print(answer)
    return answer
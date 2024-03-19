def solution(A, B):
    
    count = 0
    A = list(A)
    B = list(B)
    
    if A == B:
        return 0
    else:
        N = len(A)
        for i in range(N):
            tmp = A.pop(-1)
            A.insert(0, tmp)

            if A == B:
                count = i + 1
                break

        if count == 0:
            return -1
        else:
            return count
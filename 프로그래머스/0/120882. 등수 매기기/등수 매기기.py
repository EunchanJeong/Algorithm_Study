def solution(score):
    answer = []
    for idx, s in enumerate(score):
        score[idx] = sum(s)/len(s)
        
    tmp = score.copy()
    tmp.sort(reverse=True)
    
    for s in score:
        answer.append(tmp.index(s)+1)
    
    return answer
def solution(hp):
    answer = 0
    
    antes = [5, 3, 1]
    
    for ant in antes:
        while True:
            if hp-ant < 0:
                break
            else:
                hp -= ant
                answer += 1
        
    return answer
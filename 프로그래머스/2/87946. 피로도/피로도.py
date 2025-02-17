import itertools

def solution(k, dungeons):
    
    permutation_list = list(itertools.permutations(dungeons))
    
    answer = []   
    
    for p in permutation_list: 	
        total = 0  
        k_copy = k  
        for i, j in p:
            if i > k_copy:
                break
            else:
                k_copy = k_copy-j
                total += 1 
                
        answer.append(total)

    return max(answer)

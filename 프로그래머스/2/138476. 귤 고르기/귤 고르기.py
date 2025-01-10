from collections import Counter

def solution(k, tangerine):
    unique_set = set()
    tmp = Counter(tangerine)
    tangerine = sorted(tangerine, key=lambda x: (-tmp[x], x))
    
    count = 0
    for t in tangerine:
        count += 1

        if t not in unique_set:
            unique_set.add(t)
    
        if count == k:
            break
            
    return len(unique_set)
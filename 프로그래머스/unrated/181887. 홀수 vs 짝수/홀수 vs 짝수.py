def solution(num_list):
    sums = []
    sums.append(sum([val for i, val in enumerate(num_list) if i%2!=0]))
    sums.append(sum([val for i, val in enumerate(num_list) if i%2==0]))
    return max(sums)
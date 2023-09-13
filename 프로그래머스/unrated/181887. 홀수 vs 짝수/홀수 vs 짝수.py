def solution(num_list):
    # sums = []
    # sums.append(sum([val for i, val in enumerate(num_list) if i%2!=0]))
    # sums.append(sum([val for i, val in enumerate(num_list) if i%2==0]))
    return max(sum(num_list[::2]), sum(num_list[1::2]))
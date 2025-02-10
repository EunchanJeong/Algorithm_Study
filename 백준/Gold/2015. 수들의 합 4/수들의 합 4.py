import sys
input = sys.stdin.readline


n, k = map(int, input().split())
input_data = list(map(int, input().split()))

sum_dict = {0: 1}

sum_num = 0
answer = 0

for i in input_data:
    sum_num += i
    
    if sum_num - k in sum_dict.keys():
        answer += sum_dict[sum_num - k]

    sum_dict[sum_num] = sum_dict.get(sum_num, 0) + 1

print(answer)
N = int(input())

def sum_nums(tmp):
    result = 0
    for i in tmp:
        if i.isdigit():
            result += int(i)
    
    return result

inputs = []
for _ in range(N):
    inputs.append(input())

inputs.sort(key=lambda x:(len(x), sum_nums(x), x))

for i in inputs:
    print(i)
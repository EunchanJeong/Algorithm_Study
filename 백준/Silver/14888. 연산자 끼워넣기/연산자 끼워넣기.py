import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

result_max = -int(1e9)
result_min = int(1e9)
def dfs(result, count, add, sub, mul, div):
    global result_max
    global result_min

    if count == N:
        result_max = max(result_max, result)
        result_min = min(result_min, result)

    if add > 0:
        dfs(result + nums[count], count+1, add-1, sub, mul, div)
    if sub > 0:
        dfs(result - nums[count], count+1, add, sub-1, mul, div)
    if mul > 0:
        dfs(result * nums[count], count+1, add, sub, mul-1, div)
    if div > 0:
        dfs(int(result / nums[count]), count+1, add, sub, mul, div-1)

dfs(nums[0], 1, add, sub, mul, div)

print(result_max)
print(result_min)
M, N = map(int, input().split())
snacks = list(map(int, input().split()))

start = 1
end = max(snacks)
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    
    for snack in snacks:
        count += snack // mid
    
    if count >= M:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1
print(answer)
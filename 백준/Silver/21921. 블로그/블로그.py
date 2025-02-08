import sys
input = sys.stdin.readline

N, X = map(int, input().split())

nums = list(map(int, input().split()))

max_visit = 0
count = 0
visit = nums[0]

right = 0
left = 0

while right < N and left < N:
    if right - left + 1 == X:
        if max_visit == visit:
            count += 1
        elif max_visit < visit:
            max_visit = visit
            count = 1

        visit -= nums[left]
        left += 1

    else:
        right += 1
        if right < N:
            visit += nums[right]

if max_visit == 0:
    print('SAD')
else:
    print(max_visit)
    print(count)
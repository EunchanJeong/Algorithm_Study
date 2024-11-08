from collections import Counter

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    cnt = Counter(scores)
    count_max = max(cnt.values())
    t = [score for score, freq in cnt.items() if freq == count_max]
    print("#" + str(N) + " " + str(max(t)))    

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    students = []
    for n in range(1, N+1):
        score = list(map(int, input().split()))
        students.append((score[0] * 0.35) + (score[1] * 0.45) + (score[2] * 0.2))

    k_score = students[K-1]

    students.sort(reverse=True)
    div = N//10

    answer = grades[students.index(k_score) // div]
    print(f'#{t} {answer}')
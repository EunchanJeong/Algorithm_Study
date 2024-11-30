import sys
input = sys.stdin.readline

N = int(input())
seat = [[0] * N for _ in range(N)]

students = []
for _ in range(N**2):
    students.append(list(map(int, input().split())))

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for student in students:
    arr = []
    for i in range(N):
        for j in range(N):
            if seat[i][j] == 0:
                like = 0
                empty = 0

                for dx, dy in directions:
                    nx, ny = i + dx, j + dy

                    if 0 <= nx < N and 0 <= ny < N:
                        if seat[nx][ny] in student[1:]:
                            like += 1
                        if seat[nx][ny] == 0:
                            empty += 1
                arr.append([like, empty, i, j])

    if arr:
        arr.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
        seat[arr[0][2]][arr[0][3]] = student[0]

students.sort()

score = 0
for i in range(N):
    for j in range(N):
        result = 0

        for dx, dy in directions:
            nx, ny = i + dx, j + dy

            if 0 <= nx < N and 0 <= ny < N:
                if seat[nx][ny] in students[seat[i][j] - 1]:
                    result += 1
        if result != 0:
            score += 10 ** (result - 1)

print(score)
import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alphabets = list(input().split())
alphabets.sort()
result = []
vowel = ['a', 'e', 'i', 'o', 'u']
def check(result):
    vowel_count = 0
    for v in vowel:
        if v in result:
            vowel_count += result.count(v)

    return vowel_count >= 1 and (len(result)-vowel_count) >= 2
def backtracking(idx):
    if len(result) == L and check(result):
        print(''.join(result))
        return

    for i in range(idx, len(alphabets)):
        result.append(alphabets[i])
        backtracking(i+1)
        result.pop()

backtracking(0)
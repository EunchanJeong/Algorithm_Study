import sys
input = sys.stdin.readline

def next_permutation(s):
    s = list(s)
    n = len(s)
    
    i = n - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    
    if i == -1:
        return ''.join(s)
    
    j = n - 1
    while s[j] <= s[i]:
        j -= 1
    
    s[i], s[j] = s[j], s[i]
    s = s[:i + 1] + s[i + 1:][::-1]
    return ''.join(s)

N = int(input())

for _ in range(N):
    word = input().strip()
    next_word = next_permutation(word)
    if next_word == word:
        print(word)
    else:
        print(next_word)
S = input()

alphabets = {}
for chr in 'abcdefghijklmnopqrstuvwxyz':
    alphabets[chr] = 0
    
for chr in S:
    alphabets[chr] += 1

for num in alphabets.values():
    print(num, end=' ')
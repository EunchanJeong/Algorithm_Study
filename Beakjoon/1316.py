size = int(input())

count = 0

words = []

for i in range(size):
    words.append(input())

for w in words:
    error = False

    for i in range(len(w)-1):
        if w[i] != w[i+1]:
            n = w[i+1:]
            n_count = n.count(w[i])
            if n_count > 0:
                error = True

    if error == False:
        count += 1

print(count)
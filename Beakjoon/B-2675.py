size = int(input())

for i in range(size):
    enter = input()

    r = int(enter[0])
    output = ""

    for ch in enter[2:]:
        output += (ch * r)

    print(output)
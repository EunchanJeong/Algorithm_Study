import sys
input = sys.stdin.readline

N = int(input())

members = {}

for _ in range(N):
    age, name = input().split()
    age = int(age)
    if age in members:
        members[age].append(name)
    else:
        members[age] = [name]
   
members = sorted(members.items())

for member in members:
    for i in range(len(member[1])):
        print(member[0], member[1][i])
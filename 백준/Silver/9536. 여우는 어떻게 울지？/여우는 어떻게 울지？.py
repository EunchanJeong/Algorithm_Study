T = int(input())

while T != 0:
    sounds = list(input().split())
    
    animals = []
    
    while True:
        S = input()
        
        if S == 'what does the fox say?':
            break
        animal, tmp, sound = S.split()
        
        animals.append(sound)
        
    answer = [s for s in sounds if s not in animals]
    
    for a in answer:
        print(a, end=' ')
    print()
    
    T -= 1
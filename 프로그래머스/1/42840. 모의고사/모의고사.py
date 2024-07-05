def solution(answers):
    answer = []
    
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    count = 0
    a = [0, 0, 0]
    idx = [0, 0, 0]    

    while count != len(answers):
        if (count)%len(student1)==0:
            idx[0] = 0
        if (count)%len(student2)==0:
            idx[1] = 0
        if (count)%len(student3)==0:
            idx[2] = 0
        
        if student1[idx[0]] == answers[count]:
            print(student1[idx[0]])
            a[0] += 1
        if student2[idx[1]] == answers[count]:
            a[1] += 1
        if student3[idx[2]] == answers[count]:
            a[2] += 1
            
        idx[0] += 1
        idx[1] += 1
        idx[2] += 1
        count += 1
        
    a_max = max(a)
    
    for i in range(len(a)):
        if a_max == a[i]:
            answer.append(i+1)

    return answer
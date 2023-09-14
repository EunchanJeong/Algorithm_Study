def solution(todo_list, finished):
    answer = []
    
    for i, val in enumerate(finished):
        if val:
            continue
        else:
            answer.append(todo_list[i])
    return answer
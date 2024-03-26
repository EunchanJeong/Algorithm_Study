def solution(id_pw, db):
    id = id_pw[0]
    pw = id_pw[1]
    
    for i in db:
        print(i)
        if id == i[0]:
            if pw == i[1]:
                return 'login'
            else:
                return 'wrong pw'
    
    return 'fail'
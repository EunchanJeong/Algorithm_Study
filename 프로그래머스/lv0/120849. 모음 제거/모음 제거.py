def solution(my_string):
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    my_string = list(my_string)
    
    for i in vowels:
        while True:
            if i in my_string:
                my_string.pop(my_string.index(i))
            else:
                break
                
    answer = ''.join(my_string)
    return answer
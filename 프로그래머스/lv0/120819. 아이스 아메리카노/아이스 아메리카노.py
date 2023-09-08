def solution(money):
    
    coffee = money // 5500
    money = money - (coffee*5500)
    answer = [coffee, money]
    return answer
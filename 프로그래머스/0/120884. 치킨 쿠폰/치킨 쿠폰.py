def solution(chicken):
    answer = 0
    t = 0
    coupon = chicken
    
    while coupon >= 10:
        t = (coupon%10)
        service = coupon//10
        
        coupon = service + t
        
        answer += service
        
    return answer
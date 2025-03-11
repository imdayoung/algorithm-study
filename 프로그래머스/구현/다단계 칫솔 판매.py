def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = {i:0 for i in enroll}
    
    referral_dict = {}
    for i in range(n):
        referral_dict[enroll[i]] = referral[i]
    
    temp = {i:0 for i in enroll}
    
    for i in range(len(seller)):
        name = seller[i]
        money = amount[i] * 100
        
        while True:
            to_up = int(money * 0.1)
            to_me = money - to_up
            temp[name] += to_me
            
            name = referral_dict[name]
            money = to_up
            
            if name == '-' or to_up == 0:
                break
                
    for name in enroll:
        answer[name] += temp[name]

    return [i for i in answer.values()]
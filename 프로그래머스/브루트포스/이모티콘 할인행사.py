plus_registered = 0
purchased_price = 0


def register_or_not(discount_rates, m, users, emoticons):
    plus_registered_temp = 0
    purchased_price_temp = 0

    for user in users:
        temp = 0
        min_discount = user[0]
        limit_price = user[1]

        for i in range(m):
            if discount_rates[i] >= min_discount:
                temp += emoticons[i] * (1 - discount_rates[i] * 0.01)
        if temp >= limit_price:
            plus_registered_temp += 1
        else:
            purchased_price_temp += temp
    
    return plus_registered_temp, purchased_price_temp


def get_max_register(discount_rates, m, users, emoticons):
    global plus_registered
    global purchased_price
    
    purchased_price_temp = 0
    plus_registered_temp = 0
    
    if len(discount_rates) == m:
        plus_registered_temp, purchased_price_temp = register_or_not(discount_rates, m, users, emoticons)
        if plus_registered_temp > plus_registered or (plus_registered_temp == plus_registered and purchased_price_temp > purchased_price):
            plus_registered = plus_registered_temp
            purchased_price = purchased_price_temp
        return
    
    for rate in [10, 20, 30, 40]:
        get_max_register(discount_rates + [rate], m, users, emoticons)
        
        
def solution(users, emoticons):
    get_max_register([], len(emoticons), users, emoticons)
    return [plus_registered, int(purchased_price)]
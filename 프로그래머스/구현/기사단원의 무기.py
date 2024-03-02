def solution(number, limit, power):
    weapon = []
    
    for i in range(1, number + 1):
        temp = 0
        
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                temp += 1
        temp *= 2
        if i ** 0.5 == int(i ** 0.5):
            temp -= 1
                
        if temp > limit: weapon.append(power)
        else: weapon.append(temp)
        
    return sum(weapon)
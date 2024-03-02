from collections import Counter

def solution(want, number, discount):
    answer = 0
    wants = sorted([(want[i], number[i]) for i in range(len(want))])
    
    for i in range(len(discount) - 9):
        discounts = discount[i:i+10]
        lists = sorted(Counter(discounts).items())
        if lists == wants:
            answer += 1
    
    return answer
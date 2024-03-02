def solution(bandage, health, attacks):
    CONTINUOUS_TIME = bandage[0]
    RECOVER_PER_SECOND = bandage[1]
    RECOVER_ADDITION = bandage[2]
    ATTACK_TIME, ATTACK_AMOUNT = 0, 1
    
    health_now = health
    attack_cnt = 0
    continuous = 0
    
    for i in range(attacks[-1][ATTACK_TIME] + 1):
        # 공격 받을 시간인 경우
        if attacks[attack_cnt][ATTACK_TIME] == i:
            continuous = 0
            health_now -= attacks[attack_cnt][ATTACK_AMOUNT]
            attack_cnt += 1
            if health_now <= 0:
                return -1
            
        # 공격 받을 시간이 아닌 경우
        else:
            # 체력 회복
            health_now += RECOVER_PER_SECOND
            continuous += 1
            # 시전시간만큼 연속 붕대 감기 성공
            if continuous == CONTINUOUS_TIME:
                continuous = 0
                health_now += RECOVER_ADDITION
            # 최대 체력 초과 불가
            if health_now > health:
                health_now = health
    return health_now
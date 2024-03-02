import math
from collections import defaultdict


# 사용 시간 리턴
def get_use_time(in_hour, in_min, out_hour, out_min):
    if out_min >= in_min:
        use_hour = out_hour - in_hour
        use_min = out_min - in_min
    else:
        use_hour = out_hour - in_hour - 1
        use_min = out_min - in_min + 60

    return use_hour * 60 + use_min


def solution(fees, records):
    BASED_TIME, BASED_FEE, PER_TIME, FEE_PER_TIME = fees[0], fees[1], fees[2], fees[3]

    in_inform = {}
    total_use_time = defaultdict(int)
    charge_fee = defaultdict(int)

    # 누적 주차 시간 계산
    for record in records:
        time, car_number, state = record.split()
        if state == "IN":
            in_inform[car_number] = [int(time[:2]), int(time[3:])]
        else:
            total_use_time[car_number] += get_use_time(in_inform[car_number][0], in_inform[car_number][1], int(time[:2]), int(time[3:]))
            del in_inform[car_number]

    for car_number in in_inform.keys():
        total_use_time[car_number] += get_use_time(in_inform[car_number][0], in_inform[car_number][1], 23, 59)

    # 청구 요금 계산
    for car_number, use_time in total_use_time.items():
        if use_time <= BASED_TIME:
            charge_fee[car_number] += BASED_FEE
        else:
            charge_fee[car_number] += BASED_FEE + math.ceil((use_time - BASED_TIME) / PER_TIME) * FEE_PER_TIME

    return list(dict(sorted(charge_fee.items())).values())
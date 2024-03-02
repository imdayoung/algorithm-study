def solution(s):
    trans_cnt = 0
    all_zero_cnt = 0
    
    while s != "1":
        zero_cnt = 0
        s_len = len(s)
        for num in s:
            if num == "0":
                zero_cnt += 1
        s = bin(s_len - zero_cnt)[2:]
        trans_cnt += 1
        all_zero_cnt += zero_cnt

    return [trans_cnt, all_zero_cnt]
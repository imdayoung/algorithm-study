def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    # 시작시간과 끝시간을 초단위로 변환
    start_time = h1 * 3600 + m1 * 60 + s1
    end_time = h2 * 3600 + m2 * 60 + s2  

    # next기준으로 계산할거니 포함되지 않는 시작시간 00시, 12시 미리 카운팅
    if start_time == 0 * 3600 or start_time == 12 * 3600:
        answer += 1

    while start_time < end_time:
        # 시침 1시간 = 30도 -> 1초에 30/3600도 즉, 1/120도 이동
        # 분침 1분 = 6도 -> 1초에 6/60도 즉, 1/10도 이동
        # 초침 1초 = 6도 -> 1초에 6도 이동 
        h_before_angle = start_time / 120 % 360
        m_before_angle = start_time / 10 % 360
        s_before_angle = start_time * 6 % 360

        # 다음 위치가 360도가 아닌 0도로 계산되어 카운팅에 포함되지 않는 경우 방지
        # 이동했을 때 지나쳤거나 같아졌는지를 비교하는 것이므로 현재위치는 해줄 필요없음
        h_after_angle = 360 if (start_time + 1) / 120 % 360 == 0 else (start_time + 1) / 120 % 360
        m_after_angle = 360 if (start_time + 1) / 10 % 360 == 0 else (start_time + 1) / 10 % 360
        s_after_angle = 360 if (start_time + 1) * 6 % 360 == 0 else (start_time + 1) * 6 % 360

        if s_before_angle < h_before_angle and s_after_angle >= h_after_angle:
            answer += 1
        if s_before_angle < m_before_angle and s_after_angle >= m_after_angle:
            answer += 1
        # 시침/분침과 동시에 겹쳤을 때 중복카운팅 제외 
        if s_after_angle == h_after_angle and h_after_angle == m_after_angle:
            answer -= 1

        start_time += 1

    return answer

# def solution(h1, m1, s1, h2, m2, s2):
#     answer = 0
    
#     h_angle = h1 * 30 + m1 * 0.5 + s1 * 0.01
#     m_angle = m1 * 6 + s1 * 0.1
#     s_angle = s1 * 6

#     if (h_angle == s_angle) ^ (m_angle == s_angle):
#         answer += 1
        
#     while True:
#         # 초침과 시침의 각도 비교
#         if h_angle > s_angle:   h_flag_before = 1
#         else:                   h_flag_before = 2
            
#         # 초침과 분침의 각도 비교
#         if m_angle > s_angle:   m_flag_before = 1
#         else:                   m_flag_before = 2
        
#         # 1초 경과 후 시간
#         s1 += 1
#         if s1 == 60:
#             s1 = 0
#             m1 += 1
#             if m1 == 60:
#                 m1 = 0
#                 h1 += 1
            
#         h_angle = h1 * 30 + m1 * 0.5 + s1 * 0.01
#         m_angle = m1 * 6 + s1 * 0.1
#         s_angle = s1 * 6

#         # 1초 경과 후 초침과 시침의 각도 비교
#         if h_angle > s_angle:   h_flag_after = 1
#         else:                   h_flag_after = 2
        
#         # 1초 경과 후 초침과 분침의 각도 비교
#         if m_angle > s_angle:   m_flag_after = 1
#         else:                   m_flag_after = 2
            
#         # 1초 경과 후 초침이 시침, 분침과 만나는 지 확인
#         h_alarm, m_alarm = False, False
#         if h_flag_before != h_flag_after:   h_alarm = True
#         if m_flag_before != m_flag_after:   m_alarm = True

#         # 1초 경과 후 초침이 시침 또는 분침 하나랑 겹치는 경우
#         if h_alarm ^ m_alarm:
    #         print(f"{h1}시 {m1}분 {s1}초로 넘어가는 순간 초침이 어떤거랑 겹침")
    #         answer += 1

    #     # 1초 경과 후 초침이 시침 또는 분침 모두와 겹치는 경우
    #     # 같은 시간에 초침, 분침, 시침이 겹치는 지 확인
    #     # -> 같은 시간에 겹치는 게 아니라면 answer += 2
    #     # -> 같은 시간에 경우 answer += 0
    #     elif h_alarm and m_alarm:
    #         print(f"{h1}시 {m1}분 {s1}초로 넘어가는 순간 모두 겹침")
    #         answer += 2

    #     if h1 == h2 and m1 == m2 and s1 == s2:
    #         break

    # return answer
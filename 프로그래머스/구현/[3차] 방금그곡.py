def solution(m, musicinfos):
    answer = []

    for musicinfo in musicinfos:
        start_time, end_time, title, melody = musicinfo.split(",")

        # 라디오에서 재생된 시간 구하기
        played_time = 0
        start_hour, start_min = int(start_time[:2]), int(start_time[3:])
        end_hour, end_min = int(end_time[:2]), int(end_time[3:])
        if end_min > start_min:
            played_time = (end_hour - start_hour - 1) * 60 + (60 - start_min) + end_min
        else:
            played_time = (end_hour - start_hour) * 60 + (end_min - start_min)

        # 멜로디를 리스트로 구분하기
        melody_list = []
        for i in range(len(melody)):
            if melody[i] == "#":
                melody_list[-1] = melody_list[-1] + "#"
            else:
                melody_list.append(melody[i])

        # 라디오에서 재생된 멜로디 구하기
        played_melody = []
        melody_len = len(melody_list)
        if melody_len > played_time:
            played_melody = melody_list[:played_time]
        else:
            played_melody = melody_list * (played_time // melody_len) + melody_list[:played_time % melody_len]

        # 네오가 들은 음악을 리스트로 표현
        listened = []
        for i in range(len(m)):
            if m[i] == "#":
                listened[-1] = listened[-1] + "#"
            else:
                listened.append(m[i])
        listened_len = len(listened)

        # 들은 멜로디가 포함되어 있는 지 확인
        for i in range(len(played_melody) - listened_len + 1):
            if played_melody[i:i + listened_len] == listened:
                answer.append((title, played_time))
                break

    if len(answer) == 0:
        return "(None)"
    else:
        answer.sort(key = lambda x:-x[1])
        return answer[0][0]
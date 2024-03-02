def solution(record):
    answer = []
    answer_temp = []
    users = {}

    for rec in record:
        r = rec.split()
        action = r[0]
        if action == "Enter":
            uid, nickname = r[1], r[2]
            users[uid] = nickname
            sentence = uid + " 님이 들어왔습니다."
            answer_temp.append(sentence)

        elif action == "Leave":
            uid = r[1]
            sentence = uid + " 님이 나갔습니다."
            answer_temp.append(sentence)

        else:
            uid, changed_nickname = r[1], r[2]
            users[uid] = changed_nickname

    for temp in answer_temp:
        t = temp.split()
        answer.append(users[t[0]] + t[1] + " " + t[2])

    return answer
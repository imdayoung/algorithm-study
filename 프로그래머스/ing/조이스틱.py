# 67M 52S 겨우 풀었는데 실패해서 질문게시판 봄 ㅜㅜ 백트래킹으로 커서를 어디로 이동해야하는 지 정해야 한다고 ..?
# + 28M 53S -> 96M 45S
def move_joystick(target):
    ascii_target = ord(target)
    if ascii_target < 78:
        return abs(ascii_target - 65)
    else:
        return abs(ascii_target - 91)

"""
def solution(name):
    answer = 0

    n = len(name)
    cur_name = ['A' for _ in range(n)]
    
    cnt = 0
    to_change = []
    for i in range(n):
        if name[i] != 'A':
            to_change.append(i)
            cnt += 1

    # 현재 커서의 위치
    cur = 0
    
    # 바꿔야할 알파벳이 존재
    while cnt > 0:
        # 이미 문자가 완성된 경우 조이스틱 이동
        if cur_name[cur] == name[cur]:
            next_cur = 0
            distance = 20
            for i in to_change:
                # 현재 커서에서 i번째 인덱스까지 가기 위해 이동해야하는 거리
                temp = min(abs(i - cur), n - abs(i - cur))
                if temp < distance:
                    distance = temp
                    next_cur = i

            answer += distance
            cur = next_cur

        # 문자 바꾸기
        else:
            answer += move_joystick(name[cur])
            cur_name[cur] = name[cur]
            to_change.remove(cur)
            cnt -= 1


    return answer

    
def cursor_move(cur, to_change, cnt, n):
    global aa

    for i in range(n):
        if to_change[i]:
            break
    # 바꿀 문자가 더이상 없는 경우
    else:
        aa = min(aa, cnt)
        return 

    next_cur_left = (cur - 1) % n
    next_cur_right = (cur + 1) % n

    while not to_change[next_cur_left]:
        next_cur_left -= 1
        next_cur_left %= n
    while not to_change[next_cur_right]:
        next_cur_right += 1
        next_cur_right %= n

    to_change[next_cur_left] = False
    cursor_move(next_cur_left, to_change, cnt + min(abs(next_cur_left - cur), n - abs(next_cur_left - cur)), n)
    to_change[next_cur_left] = True
    to_change[next_cur_right] = False
    cursor_move(next_cur_left, to_change, cnt + min(abs(next_cur_left - cur), n - abs(next_cur_left - cur)), n)
    to_change[next_cur_right] = True


def solution(name):
    n = len(name)
    answer = 0

    to_change = [True for _ in range(n)]
    to_change[0] = False
    for i in range(n):
        # i + 1번째 단어가 A이면 조작하지 않아도 됨
        if name[i] == 'A':
            to_change[i] = False
    
    # 커서를 움직이는 데 필요한 최소 조작 횟수
    cursor_move(0, to_change, 0, n)
    print("커서 이동 횟수:", aa)
    answer += aa

    # 문자를 변경하는 데 필요한 조작 횟수
    if name[0] != 'A':
        answer += move_joystick(name[0])
    for i in range(n):
        if to_change[i]:
            answer += move_joystick(name[i])

    return answer

aa = 20
"""


def solution(name):
    
    return 1


print(solution("JEROEN"))
# 56
print(solution("JAN"))
# 23
print(solution('AABABAAAAABA'))
# 10